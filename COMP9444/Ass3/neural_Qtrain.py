import sys
import gym
import tensorflow as tf
import numpy as np
import random
import datetime

"""
Hyper Parameters
"""
GAMMA = 1.0                  # discount factor for target Q
INITIAL_EPSILON = 0.1        # starting value of epsilon
FINAL_EPSILON = 0.01         # final value of epsilon
EPSILON_DECAY_STEPS = 100
REPLAY_SIZE = 100000          # experience replay buffer size
BATCH_SIZE = 256              # size of minibatch
TEST_FREQUENCY = 10           # How many episodes to run before visualizing test accuracy
SAVE_FREQUENCY = 1000         # How many episodes to run before saving model (unused)
NUM_EPISODES = 500           # Episode limitation
EP_MAX_STEPS = 300            # Step limitation in an episode
NUM_TEST_EPS = 10             # The number of test iters (with epsilon set to 0) to run every TEST_FREQUENCY episodes
LR = 0.01                     # Learning rate
HIDDEN_NODES = [24, 48]       # Hidden layers, H3 = 72
REG_FACTOR = 0.001

# Initialization for discrete
def init(env, env_name):
    global replay_buffer, epsilon
    replay_buffer = []
    epsilon = INITIAL_EPSILON
    state_dim = env.observation_space.shape[0]
    action_dim = env.action_space.n
    return state_dim, action_dim


# Build network
def get_network(state_dim, action_dim, hidden_nodes=HIDDEN_NODES):

    # init variables
    state_in = tf.placeholder("float", [None, state_dim])
    action_in = tf.placeholder("float", [None, action_dim])  
    target_in = tf.placeholder("float", [None])  # q value for the target network
    c_names = ['eval_net_params', tf.GraphKeys.GLOBAL_VARIABLES]
    w_initializer = tf.random_normal_initializer(0., 0.01)
    b_initializer = tf.constant_initializer(0.01) 

    # Build network
    H1, H2 = HIDDEN_NODES[0], HIDDEN_NODES[1]
    l = tf.contrib.layers.fully_connected(state_in, H1, activation_fn=tf.nn.tanh)
    l = tf.contrib.layers.fully_connected(l, H2, activation_fn=tf.nn.tanh)
    l_final = tf.contrib.layers.fully_connected(l, action_dim, activation_fn=None)

    # Get final q_values and q_selected_action
    q_values = l_final
    q_selected_action = tf.reduce_sum(tf.multiply(q_values, action_in), reduction_indices=1)
    # Loss function
    loss = tf.reduce_mean(tf.square(target_in - q_selected_action))
    # Regularization
    # for w in [w1, w2, w3]: loss += REG_FACTOR * tf.reduce_sum(tf.square(w))
    # Optimizer
    optimise_step = tf.train.AdamOptimizer(LR).minimize(loss)
    # Save summary
    train_loss_summary_op = tf.summary.scalar("TrainingLoss", loss)
    return state_in, action_in, target_in, q_values, q_selected_action, loss, optimise_step, train_loss_summary_op


def init_session():
    global session, writer
    session = tf.InteractiveSession()
    session.run(tf.global_variables_initializer())
    # Setup Logging
    logdir = "tensorboard/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + "/"
    writer = tf.summary.FileWriter(logdir, session.graph)


# Random action
def get_action(state, state_in, q_values, epsilon, test_mode, action_dim):
    Q_estimates = q_values.eval(feed_dict={state_in: [state]})[0]
    epsilon_to_use = 0.0 if test_mode else epsilon
    if random.random() < epsilon_to_use:
        action = random.randint(0, action_dim - 1)
    else:
        action = np.argmax(Q_estimates)
    return action

# For discrete function, do not need to change
def get_env_action(action):
    """
    Modify for continous action spaces that you have discretised, see hints in
    `init()`
    """
    return action


def update_replay_buffer(replay_buffer, state, action, reward, next_state, done,
                         action_dim):
    # one-hot action
    one_hot_action = np.zeros([action_dim])
    one_hot_action[action] = 1
    # append to buffer
    replay_buffer.append([state, one_hot_action, reward, next_state, done])
    # Ensure replay_buffer doesn't grow larger than REPLAY_SIZE
    if len(replay_buffer) > REPLAY_SIZE:
        replay_buffer.pop(0)
    return None


def do_train_step(replay_buffer, state_in, action_in, target_in,
                  q_values, q_selected_action, loss, optimise_step,
                  train_loss_summary_op, batch_presentations_count):
    minibatch = random.sample(replay_buffer, BATCH_SIZE)
    target_batch, state_batch, action_batch = \
        get_train_batch(q_values, state_in, minibatch)

    summary, _ = session.run([train_loss_summary_op, optimise_step], feed_dict={
        target_in: target_batch,
        state_in: state_batch,
        action_in: action_batch
    })
    writer.add_summary(summary, batch_presentations_count)


def get_train_batch(q_values, state_in, minibatch):

    # get batch
    state_batch = [data[0] for data in minibatch]
    action_batch = [data[1] for data in minibatch]
    reward_batch = [data[2] for data in minibatch]
    next_state_batch = [data[3] for data in minibatch]
    
    # get target batch
    target_batch = []
    Q_value_batch = q_values.eval(feed_dict={ state_in: next_state_batch })
    for i in range(0, BATCH_SIZE):
        sample_is_done = minibatch[i][4]
        if sample_is_done:
            target_batch.append(reward_batch[i])
        else:
            # set the target_val to the correct Q value update
            target_val = reward_batch[i] + GAMMA * np.max(Q_value_batch[i])
            target_batch.append(target_val)
    return target_batch, state_batch, action_batch



def qtrain(env, state_dim, action_dim,
           state_in, action_in, target_in, q_values, q_selected_action,
           loss, optimise_step, train_loss_summary_op,
           num_episodes=NUM_EPISODES, ep_max_steps=EP_MAX_STEPS,
           test_frequency=TEST_FREQUENCY, num_test_eps=NUM_TEST_EPS,
           final_epsilon=FINAL_EPSILON, epsilon_decay_steps=EPSILON_DECAY_STEPS,
           force_test_mode=False, render=True):
    global epsilon
    # Record the number of times we do a training batch, take a step, and
    # the total_reward across all eps
    batch_presentations_count = total_steps = total_reward = 0

    # [Yunqiu Xu] add test for last 100 consecutive steps
    consecutive_rewards = []
    best_record = 0
    best_ep = 0

    for episode in range(num_episodes):
        # initialize task
        state = env.reset()
        # if render: env.render()

        # Yunqiu Xu : change epsilon decay
        epsilon -= (epsilon - final_epsilon) / epsilon_decay_steps
        # epsilon = max(final_epsilon, min(epsilon, 1 - np.log10(total_steps + 1) * epsilon_decay_steps))
        if episode % 10 == 0:
            print("Current epsilon: {}".format(epsilon))


        # in test mode we set epsilon to 0
        test_mode = force_test_mode or ((episode % test_frequency) < num_test_eps and episode > num_test_eps)
        # if test_mode: print("Test mode (epsilon set to 0.0)")

        ep_reward = 0
        for step in range(ep_max_steps):
            total_steps += 1

            # get an action and take a step in the environment
            action = get_action(state, state_in, q_values, epsilon, test_mode,
                                action_dim)
            env_action = get_env_action(action)
            next_state, reward, done, _ = env.step(env_action)
            ep_reward += reward

            # display the updated environment
            # if render: env.render()  # comment this line to possibly reduce training time

            # add the s,a,r,s' samples to the replay_buffer
            update_replay_buffer(replay_buffer, state, action, reward,
                                 next_state, done, action_dim)
            state = next_state

            # perform a training step if the replay_buffer has a batch worth of samples
            if (len(replay_buffer) > BATCH_SIZE):
                do_train_step(replay_buffer, state_in, action_in, target_in,
                              q_values, q_selected_action, loss, optimise_step,
                              train_loss_summary_op, batch_presentations_count)
                batch_presentations_count += 1

            if done:    
                # Yunqiu Xu
                # print("Break step: " + str(total_steps))
                # print("-----")
                break

        total_reward += ep_reward

        test_or_train = "test" if test_mode else "train"
        # print("end {0} episode {1}, ep reward: {2}, ave reward: {3}, \
        #     Batch presentations: {4}, epsilon: {5}".format(
        #     test_or_train, episode, ep_reward, total_reward / (episode + 1),
        #     batch_presentations_count, epsilon
        # ))

        # YUNQIU XU
        if len(consecutive_rewards) < 100:
            consecutive_rewards.append(ep_reward)
        else:
            consecutive_rewards.pop(0)
            consecutive_rewards.append(ep_reward)
            curr = np.mean(consecutive_rewards)
            # print("Last 100 avg ep_reward : {}".format(curr))
            if best_record < curr:
                best_record = curr
                best_ep = episode
            if episode % 25 == 0:
                print("Current ep : {}, last 100 avg ep_reward : {}".format(episode, curr))
                print("Till now best record : {}, at episode {}".format(best_record, best_ep))
                print("=====")

            if curr > 195:
                print("###   Solved at ep {}, congratulations!   ###".format(episode))
                exit()

def setup():
    default_env_name = 'CartPole-v0'
    # default_env_name = 'MountainCar-v0'
    # default_env_name = 'Pendulum-v0'
    # if env_name provided as cmd line arg, then use that
    env_name = sys.argv[1] if len(sys.argv) > 1 else default_env_name
    env = gym.make(env_name)
    state_dim, action_dim = init(env, env_name)
    network_vars = get_network(state_dim, action_dim)
    init_session()
    return env, state_dim, action_dim, network_vars


def main():
    env, state_dim, action_dim, network_vars = setup()
    qtrain(env, state_dim, action_dim, *network_vars, render=False)


if __name__ == "__main__":
    main()
