# -*- coding: utf-8 -*-
'''utility for parameters of lightgbm

'''
from lightgbm import LGBMRegressor
import hyperopt.hp as hp
from hyperopt.pyll.base import scope


def get_default_params(
    verbose=-1,
):
    '''get default parameters of LGBMRegressor

    keyword auguments:
    verbose -- -1(default)

    return: dict of parameters

    '''
    params = LGBMRegressor().get_params()
    params["verbose"] = -1
    return params


def get_quniform_space(
    label,
    low,
    high,
    q,
):
    '''get quniform space for hyperopt

    keyword auguments:
    label -- string of parameter name
    low -- int
    high -- int
    q -- int

    return:
    space for hyperopt

    '''
    space = scope.int(
        hp.quniform(
            label,
            low,
            high,
            q,
        )
    )
    return space


def get_num_leaves_space(
    low=7,
    high=63,
    q=1,
):
    '''get space for num_leaves of quniform

    keyword auguments:
    low -- 7(default)
    high -- 63(default)
    q -- 1(default)

    return:
    space for num_leaves

    '''
    return get_quniform_space(
        "num_leaves",
        low,
        high,
        q,
        )


def set_num_leaves_space(
    space,
    label_space=None,
):
    '''set space for num_leaves

    keyword auguments:
    space -- space for set
    label_space -- space of num_leaves (default=None)
                   IF None : set space return of  get_num_leaves_space()
    return: None

    '''
    if label_space is None:
        label_space = get_num_leaves_space()
    space["num_leaves"] = label_space


def get_min_child_samples_space(
    low=4,
    high=40,
    q=1,
):
    '''get space for min_child_samples of quniform

    keyword auguments:
    low -- 4(default)
    high -- 60(default)
    q -- 1(default)

    return:
    space for min_child_samples

    '''
    return get_quniform_space(
        "min_child_samples",
        low,
        high,
        q,
        )


def set_min_child_samples_space(
    space,
    label_space=None,
):
    '''set space for min_child_samples

    keyword auguments:
    space -- space for set
    label_space -- space of num_leaves (default=None)
                   IF None : set space return of  get_min_child_samples_space()
    return: None

    '''
    if label_space is None:
        label_space = get_min_child_samples_space()
    space["min_child_samples"] = label_space


def get_reg_alpha_space(
    low=0,
    high=1,
):
    '''get space for reg_alpha of uniform

    keyword auguments:
    low -- 0(default)
    high -- 1(default)

    return:
    space

    '''
    return hp.uniform(
        "reg_alpha",
        low,
        high,
        )


def set_reg_alpha_space(
    space,
    label_space=None,
):
    '''set space for reg_alpha

    keyword auguments:
    space -- space for set reg_alpha
    label_space -- space of  (default=None)
                   IF None : set space return of  get_reg_alpha_space()
    return: None

    '''
    if label_space is None:
        label_space = get_reg_alpha_space()
    space["reg_alpha"] = label_space

def get_reg_lambda_space(
    low=0,
    high=1,
):
    '''get space for reg_lambda of uniform

    keyword auguments:
    low -- 0(default)
    high -- 1(default)

    return:
    space

    '''
    return hp.uniform(
        "reg_lambda",
        low,
        high,
        )


def set_reg_lambda_space(
    space,
    label_space=None,
):
    '''set space for reg_lambda

    keyword auguments:
    space -- space for set reg_lambda
    label_space -- space of  (default=None)
                   IF None : set space return of  get_reg_lambda_space()
    return: None

    '''
    if label_space is None:
        label_space = get_reg_lambda_space()
    space["reg_lambda"] = label_space


def get_simple_space():
    '''get simple space
        set below label_space
            - num_leaves space
            - min_child_samples space

    return: dict of space

    '''
    space = get_default_params()
    set_num_leaves_space(space)
    set_min_child_samples_space(space)
    return space


def get_standard_space():
    '''get simple space
        set below label_space
            - num_leaves space
            - min_child_samples space
            - reg_alpha space
            - reg_lambda space

    return: dict of space

    '''
    space = get_default_params()
    set_num_leaves_space(space)
    set_min_child_samples_space(space)
    set_reg_alpha_space(space)
    set_reg_lambda_space(space)
    return space
