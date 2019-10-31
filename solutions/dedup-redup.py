from collections import OrderedDict
import os

# Complete the functions below.
CHUNK_SIZE = 1024
INT_SIZE = 32   
ENCODING = 'cp1252'


def dedup(input_file_path, output_file_path):
    # Open the files
    try:
        in_file = open(input_file_path, 'rb')
        out_file = open(output_file_path, 'wb')
    except Exception:
        print('File open failed!')
    
    # Find the file sizes
    in_file_size = os.path.getsize(input_file_path)
    n_chunks = int(in_file_size / CHUNK_SIZE)
    
    # We maintain:
    #  - unique_chunk_map: Map of chunks to indices.
    #  - chunk_index_list: List of indices in the unique_chunk map.
    unique_chunk_map = OrderedDict()
    chunk_index_list = [None] * n_chunks
    
    # read the file chunk by chunk
    for ix in range(n_chunks):
        chunk = in_file.read(CHUNK_SIZE)

        # If not found earlier, insert in the map.
        if chunk not in unique_chunk_map:
            unique_chunk_map[chunk] = len(unique_chunk_map)
        
        # Add the index of the unique chunk found
        chunk_index_list[ix] = unique_chunk_map[chunk]

    # Write the number of chunks to the BEGINNING of the file
    out_file.write(len(unique_chunk_map).to_bytes(INT_SIZE, byteorder='big'))
    
    for chunk in unique_chunk_map.keys():
        out_file.write(chunk)
        
    out_file.write(','.join([str(x) for x in chunk_index_list]).encode(ENCODING))

    # Close the files
    in_file.close()
    out_file.close()
    

def redup(input_file_path, output_file_path):
    # Open the files
    try:
        in_file = open(input_file_path, 'rb')
        out_file = open(output_file_path, 'wb')
    except Exception:
        print('File open failed!')
    
    # We maintain:
    #  - unique_chunk_map: Map of chunks to indices.
    #  - chunk_index_list: List of indices in the unique_chunk map.
    unique_chunk_map_inv = OrderedDict()
    
    # Get the number of unique chunks from the first INT_SIZE bytes of the file
    n_unique_chunks = int.from_bytes(in_file.read(INT_SIZE), byteorder='big')
    
    # Get all the unique chunks
    for ix in range(n_unique_chunks):
        unique_chunk_map_inv[ix] = in_file.read(CHUNK_SIZE)

    # Get the list: the rest of the bytes would just contain that!
    list_as_str = in_file.read().decode(ENCODING)
    chunk_index_list = [int(x) for x in list_as_str.split(',')]
    
    
    # Write the chunks!
    for chunk_index in chunk_index_list:
        out_file.write(unique_chunk_map_inv[chunk_index])

    # Close the files
    in_file.close()
    out_file.close()
    
    with open(output_file_path, 'rb') as infile:
        output_contents = infile.read()
    
    return True
