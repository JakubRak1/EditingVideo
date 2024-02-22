import os
import imageio[ffmpeg] as ffmpeg

#   Single File
def convert_video(input_file, to_file):
    input_folder = '../../videos/input'
    input_file_path = os.path.join(input_folder,input_file)
    #   Check for errors
    if not os.path.exists(input_file_path):
        raise ValueError('No such file or input file is missing')
    output_folder = '../../videos/output'
    root, extension = os.path.split(input_file)
    output_file_name = f'{root}.{to_file}'
    output_file_path = os.path.join(output_folder, output_file_name)
    
    #   Open writer and reader
    writer = ffmpeg.get_writer(output_file_path, format=to_file)
    reader = ffmpeg.get_reader(input_file_path) 

    try:
        # Iterate over each frame and write it to the file
        for frame in reader:
            writer.append_data(frame)
        print(f"Conversion successful {to_file} file saved as '{output_file_name}'.")
    except Exception as e:
        print(f"Error during conversion: {e}")
    finally:
        # Close the writer and reader
        writer.close()
        reader.close()


#   Single File
def convert_videos (input_files, to_file):
    for input_file in input_files:
        input_folder = '../../videos/output'
        input_file_path = os.path.join(input_folder,input_file)
        #   Check for errors
        if not os.path.exists(input_file_path):
            raise ValueError('No such file or input file is missing')
        output_folder = '../../videos/output'
        root, extension = os.path.split(input_file)
        output_file_name = f'{root}.{to_file}'
        output_file_path = os.path.join(output_file, output_file_name)
        
        #   Open writer and reader
        writer = ffmpeg.get_writer(output_file_path, format=to_file)
        reader = ffmpeg.get_reader(input_file_path) 

        try:
            # Iterate over each frame and write it to the file
            for frame in reader:
                writer.append_data(frame)
            print(f"Conversion successful {to_file} file saved as '{output_file_name}'.")
        except Exception as e:
            print(f"Error during conversion: {e}")
        finally:
            # Close the writer and reader
            writer.close()
            reader.close()