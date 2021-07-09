import numpy as np

def calculate(list):
    np_arr = np.array(list)
    if len(np_arr) == 9:
        pass
    else:
        raise ValueError("List must contain nine numbers.")
    try:

        np_arr_reshaped = np_arr.reshape(3,3)

        calculations = dict()
        calculations['mean'] = [np_arr_reshaped.mean(axis=0).tolist(), np_arr_reshaped.mean(axis=1).tolist(), np_arr_reshaped.mean().tolist()]
        calculations['variance'] = [np_arr_reshaped.var(axis=0).tolist(), np_arr_reshaped.var(axis=1).tolist(), np_arr_reshaped.var().tolist()]
        calculations['standard deviation'] = [np_arr_reshaped.std(axis=0).tolist(), np_arr_reshaped.std(axis=1).tolist(), np_arr_reshaped.std().tolist()]
        calculations['max'] = [np_arr_reshaped.max(axis=0).tolist(), np_arr_reshaped.max(axis=1).tolist(), np_arr_reshaped.max().tolist()]
        calculations['min'] = [np_arr_reshaped.min(axis=0).tolist(), np_arr_reshaped.min(axis=1).tolist(), np_arr_reshaped.min().tolist()]
        calculations['sum'] = [np_arr_reshaped.sum(axis=0).tolist(), np_arr_reshaped.sum(axis=1).tolist(), np_arr_reshaped.sum().tolist()]

        # for key, values in calculations.items():
        #     print(key, values)


        return calculations
    except ValueError:
        print("List must contain nine numbers.")


if __name__ == '__main__':
    print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))
    print(calculate([2,6,2,8,4,0,1,5,7]))
    print(calculate([9,1,5,3,3,3,2,9,0]))
    print(calculate([2,6,2,8,4,0,1,]))
    # print(calculate([0, 1, 2, 3, 4, 5, 6, 7]))