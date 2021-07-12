# ==============================================================================
# AppContext
# ==============================================================================


class AppContext():
    '''
    A singleton class, it acts as a global resource manager.
    '''
# |----------------------------------------------------------------------------|
# class Variables
# |----------------------------------------------------------------------------|
    _singleton = None
    _choice_panel_ui = None
    _cal_flow_ui = None
    _pick_basket_panel = None
    _drop_basket_panel = None
    _sc_panel = None
    _sf_panel = None
    _layout_controller = None

# |----------------------------------------------------------------------------|
# Constructor
# |----------------------------------------------------------------------------|
    def __init__(self, *args, **kwargs):
        pass

# |--------------------------End of Constructor-------------------------------|

# |----------------------------------------------------------------------------|
# __new__
# |----------------------------------------------------------------------------|
    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(AppContext, cls).__new__(cls, *args,
                                                            **kwargs)
        return cls._singleton

# |--------------------------End of __new__-----------------------------------|

# |----------------------------------------------------------------------------|
# get
# |----------------------------------------------------------------------------|
    @staticmethod
    def get():
        return AppContext()

# |------------------------------End of get-----------------------------------|

#|----------------------------------------------------------------------------|
# get_choice_panel_controller
# |----------------------------------------------------------------------------|
    def get_choice_panel_controller(self):
        return self._choice_panel_ui

# |-----------------------End of get_choice_panel_controller---------------|

# |------------------------------End of get-----------------------------------|

# |----------------------------------------------------------------------------|
# set_choice_panel_controller
# |----------------------------------------------------------------------------|
    def set_choice_panel_controller(self, obj):
        self._choice_panel_ui = obj

# |-----------------------End of set_choice_panel_controller--------------|

#|----------------------------------------------------------------------------|
# get_cal_flow_controller
# |----------------------------------------------------------------------------|
    def get_cal_flow_controller(self):
        return self._cal_flow_ui

# |---------------------------End of get_cal_flow_controller------------------|

#|----------------------------------------------------------------------------|
# set_cal_flow_controller
# |----------------------------------------------------------------------------|
    def set_cal_flow_controller(self, obj):
        self._cal_flow_ui = obj

# |---------------------------End of get_cal_flow_controller------------------|

#|----------------------------------------------------------------------------|
# get_pick_basket_panel_controller
# |----------------------------------------------------------------------------|
    def get_pick_basket_panel_controller(self):
        return self._pick_basket_panel

# |---------------------------End of get_pick_basket_panel_controller------------------|

#|----------------------------------------------------------------------------|
# set_pick_basket_panel_controller
# |----------------------------------------------------------------------------|
    def set_pick_basket_panel_controller(self, obj):
        self._pick_basket_panel = obj

# |-------------------End of set_pick_basket_panel_controller------------------|

#|----------------------------------------------------------------------------|
# get_drop_basket_panel_controller
# |----------------------------------------------------------------------------|
    def get_drop_basket_panel_controller(self):
        return self._pick_basket_panel

# |------------------End of get_drop_basket_panel_controller------------------|

#|----------------------------------------------------------------------------|
# set_drop_basket_panel_controller
# |----------------------------------------------------------------------------|
    def set_drop_basket_panel_controller(self, obj):
        self._pick_basket_panel = obj

# |----------------------End of set_drop_basket_panel_controller--------------|

# get_sc
# |----------------------------------------------------------------------------|
    def get_sc_panel(self):
        return self._sc_panel

# |------------------End of get_drop_basket_panel_controller------------------|

#|----------------------------------------------------------------------------|
# set_sc
# |----------------------------------------------------------------------------|
    def set_sc_panel(self, obj):
        self._sc_panel = obj

# |----------------------End of set_drop_basket_panel_controller--------------|

# get_sf
# |----------------------------------------------------------------------------|
    def get_sf_panel(self):
        return self._sf_panel

# |------------------End of get_drop_basket_panel_controller------------------|

#|----------------------------------------------------------------------------|
# set_sf
# |----------------------------------------------------------------------------|
    def set_sf_panel(self, obj):
        self._sf_panel = obj

# |----------------------End of set_drop_basket_panel_controller--------------|
# get_sf
# |----------------------------------------------------------------------------|
    def get_layout_controller(self):
        return self._layout_controller

# |------------------End of get_drop_basket_panel_controller------------------|

#|----------------------------------------------------------------------------|
