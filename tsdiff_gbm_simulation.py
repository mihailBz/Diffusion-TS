from gbm import simulate_gbm, save_tsdiff_format
import json


def main():
    simulation_parameters = [
        {'n': 252, 'M': 1000},
        {'n': 1000, 'M': 1000},
    ]

    gbm_parameters = [
        {'mu': 0.1, 'sigma': 0.2},
        {'mu': 0.3, 'sigma': 0.1},
        {'mu': 0.5, 'sigma': 0.4},
        {'mu': 0.7, 'sigma': 0.1},
        {'mu': 0.5, 'sigma': 0},
        {'mu': 0, 'sigma': 0.3},
    ]

    i = 1
    for sim_param in simulation_parameters:
        for gbm_param in gbm_parameters:
            St = simulate_gbm(S0=100, T=1, **sim_param, **gbm_param)
            save_tsdiff_format(St, f'./tsdiff_dataset/gbm-{i}.jsonl')
            # Save the parameters
            parameters = {
                'simulation_parameters': sim_param,
                'gbm_parameters': gbm_param
            }
            param_filename = f'./tsdiff_dataset/gbm-{i}-params.json'
            with open(param_filename, 'w') as f:
                json.dump(parameters, f, indent=4)

            i += 1


if __name__ == '__main__':
    main()
