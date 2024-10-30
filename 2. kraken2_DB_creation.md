# Creating the Database

You have two options for creating the database:

### 1. Downloading the Standard Database
- **Memory Requirements**: This option requires approximately **84GB of RAM**, so you may need to configure swap memory if you are short on RAM.
- **Storage Requirements**: Even though the database itself is about **500GB**, you'll need **double the storage** (approximately 1TB) during the building process.
- **Important Tips**: 
   - Use tools like `nohup` or `tmux` to prevent any disruptions during the download/build process, especially on a server.
   - **Multithreading** is recommended to speed up the process.

### 2. Downloading a Customised Database
- If you have specific needs and memory constraints, it’s recommended to build a **custom database** tailored to your target domain.
- This option allows you to build a database only for your specific use case, which can save both memory and storage.

Choose the option that best suits your requirements!


## Building a Customized Database

To build a customized database, you can download only the required reference libraries. Kraken2 provides several standard genome/protein sets that are easily accessible through `kraken2-build`:

- **archaea**: RefSeq complete archaeal genomes/proteins
- **bacteria**: RefSeq complete bacterial genomes/proteins
- **plasmid**: RefSeq plasmid nucleotide/protein sequences
- **viral**: RefSeq complete viral genomes/proteins
- **human**: GRCh38 human genome/proteins
- **fungi**: RefSeq complete fungal genomes/proteins
- **plant**: RefSeq complete plant genomes/proteins
- **protozoa**: RefSeq complete protozoan genomes/proteins
- **nr**: NCBI non-redundant protein database
- **nt**: NCBI non-redundant nucleotide database
- **UniVec**: NCBI-supplied database of vector, adapter, linker, and primer sequences that may contaminate sequencing projects or assemblies
- **UniVec_Core**: A subset of UniVec to minimize false positives in vector detection

> **Note**: When downloading the `nr` library, use the `--protein` option. `UniVec` and `UniVec_Core` are incompatible with the `--protein` option.

### Example Commands for Downloading Specific Libraries

```bash
nohup kraken2-build --download-library fungi --db <db_name> --threads 8 &
nohup kraken2-build --download-library archaea --db <db_name> --threads 8 &
nohup kraken2-build --download-library viral --db <db_name> --threads 8 &
nohup kraken2-build --download-library bacteria --db <db_name> --threads 8 &
nohup kraken2-build --download-library human --db <db_name> --threads 8 &
```
Tip: Using nohup allows the process to continue running even if the terminal session is disconnected. You can monitor the process with nohup.out.

You can add custom genomes or sequences to your database in the following format within a FASTA file:
```bash
>sequence16|kraken:taxid|<taxon ID>  Adapter sequence
CAAGCAGAAGACGGCATACGAGATCTTCGAGTGACTGGAGTTCCTTGGCACCCGAGAATTCCA
```

To add these custom sequences to your database, use the following commands:

```
kraken2-build --add-to-library chr1.fa --db <database_name>
kraken2-build --add-to-library chr2.fa --db <database_name>
```

**PLEASE NOTE DATABASE OF KRAKEN1 CANNOT BE USED WITH KRAKEN2**
ALSO IF CUSTOMIZING DATABASE WE NEED TO KEEP FILES IN SPECIFIC ORDER

Before building the database, download the necessary taxonomy files:
```bash
kraken2-build --download-taxonomy --db <db_name>
```
This will download the accession number to taxon maps, as well as the taxonomic name and tree information from NCBI.
**NOTE**: No need to download seperate accession number to taxon maps except for plasmid and nonredundant proteins.

Building database
Once you've downloaded the libraries and taxonomy data, you can build the database:

```bash
kraken2-build --build --db <database_name>
```
After successfully building database we can remove intermediate files from memory using --clean in kraken2-build
```bash
kraken2-build --clean --db <db_name>
```

### Building standard database
Creating database using standard procedure
```bash
nohup kraken2-build --standard --threads 12 --db <db_name>
```
Please check available threads in the server before running command by using 'htop' command
you can check the progress using 'cat nohup.out' which keeps log of progress

