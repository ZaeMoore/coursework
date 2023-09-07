def func2(x, y, v_x, v_y, Ftot_x, Ftot_y, t):
    xf = x + (v_x*t) + 0.5*Ftot_x*(t**2)/1000
    yf = y + (v_y*t) + 0.5*Ftot_y*(t**2)/1000

    v_xf = v_x + Ftot_x*t/1000
    v_yf = v_y + Ftot_y*t/1000

    return xf, yf, v_xf, v_yf
