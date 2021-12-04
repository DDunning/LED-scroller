import rp2

@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()                                   # type: ignore
    label("bitloop")                                # type: ignore
    out(x, 1)               .side(0)    [T3 - 1]    # type: ignore
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]    # type: ignore
    jmp("bitloop")          .side(1)    [T2 - 1]    # type: ignore
    label("do_zero")                                # type: ignore
    nop()                   .side(0)    [T2 - 1]    # type: ignore
    wrap()                                          # type: ignore
    