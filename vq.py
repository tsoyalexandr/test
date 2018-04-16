import os, sys

if len(sys.argv) == 3:
    path_to_console = str(input('Enter path to console:\n'))
    os.chdir(path_to_console)

    vq = 'VQConsole.exe'
    dra = sys.argv[1]
    media1 = os.listdir(dra)

    ele = sys.argv[2]
    media2 = os.listdir(ele)

    n = 0
    for i in range(len(media1)):
        os.system(vq + ' config.xml /in1:"' + dra + '\\' + media1[i] + '" /in2:"' + ele + '\\' + media2[i] + '" /sfx:' + str(n))
        n += 1
else:
    print('Error')
