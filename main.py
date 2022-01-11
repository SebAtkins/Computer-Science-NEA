import render, edit

def run(input, output="out.obj", seed=123456, xshift=0, zshift=0):
    edit.edit(input, output,seed, xshift, zshift)
    render.show(output)

#run("test.obj", "testOut.obj", 987654, 4, 4)