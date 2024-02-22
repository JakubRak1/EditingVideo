import os
import imageio_ffmpeg as ffmpeg
import imageio


def join_video(first_file, second_file, output_file):
    
    #Setting path to input and output
    input_folder = '../../videos/input'
    input_file_path_1 = os.path.join(input_folder,first_file)
    input_file_path_2 = os.path.join(input_folder,second_file)
    output_folder = '../../videos/output'
    output_file_path = os.path.join(output_folder, output_file)

    # Read the video clips using imageio
    clip1 = imageio.get_reader(input_file_path_1)
    clip2 = imageio.get_reader(input_file_path_2)

    # Get the metadata of the first clip
    meta_data = clip1.get_meta_data()

    # Create a writer for the output file
    writer = imageio.get_writer(output_file_path, fps=meta_data['fps'])

    # Write frames from the first clip
    for frame in clip1:
        writer.append_data(frame)

    # Write frames from the second clip
    for frame in clip2:
        writer.append_data(frame)

    # Close the clips and writer
    clip1.close()
    clip2.close()
    writer.close()