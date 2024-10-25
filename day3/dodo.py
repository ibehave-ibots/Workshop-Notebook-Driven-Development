import pandas as pd

def task_stats():
    def descriptive_stats(active_trials_csv, stats_csv):
        df = pd.read_csv(active_trials_csv)
        df_stats = df.describe().reset_index()
        df_stats.to_csv(stats_csv, index=False)  

    return {
        'actions': [(descriptive_stats,)],
        'params': [
            {
                'name': 'active_trials_csv',
                'short': 'i',
                'type': str,
                'default': 'data/active_trials.csv'
            },
            {
                'name': 'stats_csv',
                'long': 'stats_csv',
                'short': 'o',
                'type': str,
                'default': 'data/stats.csv'
            }
        ]
    }