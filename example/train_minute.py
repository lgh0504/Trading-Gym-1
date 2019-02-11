from stable_baselines import DQN
from stable_baselines.deepq.policies import MlpPolicy
import argparse
from base import init_logger, Base


def test_fake(retrain, render):
    data_path = '/data/money/source_minute.json'
    punished = retrain
    if not retrain:
        init_logger()
    times = 1 if retrain else 1
    for i in range(times):
        trainer = Base()
        info = trainer.train(data_path, DQN, MlpPolicy,
                             retrain=punished,
                             render=render,
                             train_steps=1000000,
                             save_path='fake',
                             env_params={
                                 'punished': False,
                                 'unit': 30000,
                                 'use_ta': True,
                                 'start_random': False,
                                 'ta_timeperiods': [5, 10, 15, 30]
                             },
                             rl_model_params={
                                 'verbose': 1,
                                 'learning_rate': 1e-5
                             })
        profit = info[0]['profit']['total']
        if profit > 10000:
            break


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--retrain', action="store_true", default=False)
    parser.add_argument('--render', action="store_true", default=False)

    args = parser.parse_args()

    test_fake(args.retrain, args.render)
