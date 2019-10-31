#include <fstream>

int CHUNK_SIZE = 1024;

void dedup(std::string inpath, std::string outpath)
{
    char chunk[CHUNK_SIZE];
    
    // Open input file
    std::ifstream infile(inpath);

    // Represent input file as a hash table:
    //   - key: hash of a unique 1KB chunk
    //   - value: list of indices within the file where the chunk is found
    int64_t hash;
    auto table = std::map<int64_t, std::vector<int>>();
    for (int index = 0; !infile.eof(); index++) {
        infile.read(chunk, CHUNK_SIZE);
        int count = infile.gcount();
        if (!count)
            break;
        
        // compute hash
        std::string str(chunk, count);        
        hash = std::hash<std::string>{}(str);
        
        // check if hash already exists
        auto it = table.find(hash);
        if (it == table.end()) {
            table[hash] = std::vector<int>{index};
            continue;
        }
        
        // append to list of indices
        it->second.push_back(index);
    }

    // Open output files
    std::ofstream outfile1(outpath);
    std::ofstream outfile2(outpath);

    // Write out hash table into the output file.
    // Here's how it's organized:
    //   - first four bytes: number of chunks
    //   - next 1024 bytes: first chunk
    //   - next 1024 bytes: second chunk
    //   - ...
    //   - comma-separated list of indices for first chunk (ending in newline)
    //   - comma-separated list of indices for second chunk (ending in newline)
    //   - ...
    //   - checksum
    int32_t chunk_count = table.size();
    outfile1.write((char *) &chunk_count, sizeof(int32_t));
    outfile2.seekp(sizeof(int32_t) + (chunk_count * CHUNK_SIZE));
    
    infile.clear();
    infile.seekg(0);
    while (!infile.eof()) {
        infile.read(chunk, CHUNK_SIZE);
        int count = infile.gcount();
        if (!count)
            break;
        
        // compute hash
        std::string str(chunk, count);
        int64_t hash = std::hash<std::string>{}(str);
        
        // check if chunk is still in hash table
        auto it = table.find(hash);
        if (it == table.end())
            continue;

        // get indices
        std::string indices;
        for (const auto &index : it->second) {
            if (&index != &it->second[0])
                indices += ",";
            indices += std::to_string(index);
        }
        indices += "\n";        
        
        // write out chunk and indices
        outfile1.write(chunk, CHUNK_SIZE);
        outfile2.write(indices.c_str(), indices.length());
        
        // remove chunk from hash table since it's been processed
        table.erase(it);
    }
    
    // Close files
    infile.close();
    outfile1.close();
    outfile2.close();
    
    // Calculate checksum of the output file
    std::fstream outfile(outpath, std::ios_base::in | std::ios_base::out);
    hash = 0;
    while (!outfile.eof()) {
        outfile.read(chunk, CHUNK_SIZE);
        int count = outfile.gcount();
        if (!count)
            break;

        // compute hash
        std::string str(chunk, outfile.gcount());        
        hash ^= std::hash<std::string>{}(str);
    }

    outfile.clear();
    outfile.write((char *) &hash, sizeof(int64_t));
    outfile.close();
}

bool redup(std::string inpath, std::string outpath)
{
    char chunk[CHUNK_SIZE];

    // Open input file
    std::ifstream infile(inpath, std::ifstream::ate);
    int file_size = infile.tellg();
    infile.clear();
    infile.seekg(0);

    // Compute sizes of the data vs. checksum in the input file
    int checksum_bytes = sizeof(int64_t);
    int data_bytes = file_size - checksum_bytes;

    // Verify the integrity of the input file by recomputing the checksum
    int64_t hash = 0;
    while (data_bytes > 0) {
        infile.read(chunk, std::min(CHUNK_SIZE, data_bytes));
        int count = infile.gcount();
        if (!count)
            break;
        
        std::string str(chunk, count);
        hash ^= std::hash<std::string>{}(str);
        
        data_bytes -= count;
    }
    
    // Compare checksums: recomputed vs. original
    infile.seekg(-checksum_bytes, infile.end);
    int64_t checksum;
    infile.read((char *) &checksum, sizeof(int64_t));
    infile.close();    
    if (hash != checksum)
        return false;

    int32_t chunk_count;
    
    // Open input and output files
    std::ifstream infile1(inpath);
    infile1.read((char *) &chunk_count, sizeof(int32_t));
    
    std::ifstream infile2(inpath);
    infile2.seekg(sizeof(int32_t) + chunk_count * CHUNK_SIZE);    
    
    std::ofstream outfile(outpath);
    
    // Write out the individual chunks to the output file
    std::string line;    
    for (int i = 0; i < chunk_count; i++) {
        infile1.read(chunk, CHUNK_SIZE);
        std::getline(infile2, line);
        
        std::stringstream stream(line);
        std::string index;
        while (std::getline(stream, index, ',')) {
            outfile.seekp(std::stoi(index) * CHUNK_SIZE);
            outfile.write(chunk, CHUNK_SIZE);            
        }
    }
    
    // Close input and output files
    infile1.close();
    infile2.close();
    outfile.close();
    
    return true;
}
