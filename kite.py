import sys
import interpreter

# So that you can still run this module under standard CPython, I add this
# import guard that creates a dummy class instead.
try:
    from rpython.rlib.jit import JitDriver, purefunction
except ImportError:
    from interpreter import MockJitDriver as JitDriver
    def purefunction(f): return f


jitdriver = JitDriver(greens=[], reds=[])

def main(argv):
    interpreter.start(driver=jitdriver)
    return 0

def target(driver, args):
    return main, None

def jitpolicy(driver):
    from rpython.jit.codewriter.policy import JitPolicy
    return JitPolicy()

if __name__ == '__main__':
    main(sys.argv)
