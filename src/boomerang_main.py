from boomerang import Boomerang

if __name__ == '__main__':
    # Modifiers
    create_frames = True
    output_fps = 30
    loop = 1

    # Video Input
    path = "C:\\Users\\prog\\Desktop\\Boomerang\\resources\\videos\\"
    filename = "sample"
    extension = '.mp4'

    # Output
    out_path = "C:\\Users\\prog\\Desktop\\Boomerang\\resources\\boomerangs\\"
    output_name = filename + "_boomerang"

    boomerang = Boomerang(path, filename, out_path, output_fps, output_name, extension, create_frames, loop)
    boomerang.run()