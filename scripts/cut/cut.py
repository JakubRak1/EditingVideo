import os
from ffmpeg import input, output, run
import path


# Cutting single video
def cut_video(input_file, output_file='video', start_times, end_times, extension='mkv'):
    # Checking for settings
    if len(start_times) != len(end_times):
        raise ValueError('Arrays start times and end times must have the same length.')
    # Running program    
    for index, (start_time, end_time) in enumerate(zip(start_times, end_times)):
        
        # Input folder path
        input_folder = '../../videos/output'
        input_file_path = os.path.join(input_folder,input_file)

        # Output folder path
        output_folder = '../../videos/output'
        output_file_name = f'{output_file}_{index}.{extension}'
        output_file_path = os.path.join(output_file, output_file_name)

        (
            input(input_file_path, ss=start_time)
            .output(output_file_path, c = 'copy', to = end_time-start_time)
            .run(overwrite_output=True)
        )
        print(f'File done for part {index}')
    
   
# Cutting multiply videos
def cut_videos(input_files, output_files, arr_start_time, arr_end_time, extension='mkv'):
    
    # Checking for settings
    if len(input_files) != len(arr_start_times) != len(arr_end_time):
        raise ValueError('Number of inputs files has be to equal to numbers of arrays starting,ending times.')
    if len(arr_start_times) != len(arr_end_times):
        raise ValueError('Arrays of starting times and ending times must have the amount of arrays.')
    for start_times,end_times in enumerate(zip(arr_start_start,arr_end_time)):
        if len(start_times) != len(end_times):
            raise ValueError('Arrays start times and end times must have the same length.')
    # Running program
    for index_file, input_file, start_times, end_times in enumerate(zip(input_files, arr_start_start, arr_end_time)):
        for index, (start_time, end_time) in enumerate(zip(start_times, end_times)):
        
            # Input folder path
            input_folder = '../../videos/output'
            input_file_path = os.path.join(input_folder,input_file)

            # Output folder path
            output_folder = '../../videos/output'
            output_file_name = f'{output_file}_{index_file}-{index}.{extension}'
            output_file_path = os.path.join(output_file, output_file_name)

            (
                input(input_file_path, ss=start_time)
                .output(output_file_path, c = 'copy', to = end_time-start_time)
                .run(overwrite_output=True)
            )
            print(f'File done for part {index_file}-{index}')


