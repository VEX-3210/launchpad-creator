try:
    import MainLoop as ml
    import Load as ld
    import setUp as su
    import Save as sv
except ImportError:
    print("ERROR: loading imports failed - __main__")
    input()
    exit(0)

try:
    sv.crateExampleProject()
    DetectMidi, GetFile, PathProj, mode, lp, LedValue, sleep, sleep2, Page, ButtonClick, ButtonSound = su.setUp()
    ld.LoadPro(lp, LedValue, sleep)
except:
    print("ERROR: startup app")
    exit(0)

while True:
    try:
        DetectMidi, Page = ml.MainLoop(DetectMidi, Page, lp, ButtonClick, ButtonSound)
    except:
        print('application closed')
        exit(0)
