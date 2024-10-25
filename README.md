# Kraken2_pipeline
In this repository there are steps from installing Kraken2 in conda environment to final result.

Kraken is a taxonomic sequence classifier that assigns taxonomic labels to DNA sequences by analyzing k-mers (short DNA sequences) in the query sequence. These k-mers are compared against a database that links them to the lowest common ancestor (LCA) of genomes containing that specific k-mer. The initial version of Kraken used a large indexed list of k-mer/LCA pairs to provide rapid classification, but its high memory requirements posed challenges for users. To address this, Kraken 2 was developed with enhanced efficiency and reduced memory needs.

Kraken 2 introduces several key improvements over Kraken 1. Instead of storing and querying all k-mers, Kraken 2 uses only minimizers—a smaller, representative subset of k-mers, referred to as ℓ-mers. These ℓ-mers are stored in a compact hash table, which uses a probabilistic data structure to further reduce memory consumption. This structure may occasionally result in false positives (incorrect LCA assignments or missed queries), but the error rate is low (under 1%) and can be mitigated by setting confidence scoring thresholds.

Kraken 2's database design, which stores only a fraction of possible ℓ-mers from genomic libraries, achieves high efficiency without compromising much accuracy. This approach is similar to Kraken 1's "MiniKraken" databases, but with significantly less loss in sensitivity per read. Testing shows that even reduced Kraken 2 databases maintain comparable accuracy to full-sized ones, solving a major limitation of the earlier version.
## What the project does?
The project has codes referred from original Kraken2 github file from initial installation to final report generation. So this gives the user guidance in following the project and easy understanding.
## Why the project is useful?
Following this project we can build a pipeline for analysing taxonomical classification of given raw reads.
## How users can get started with the project?
Run these codes on the server because building database requires about 100GB of storage and much computational power.
### System pre-rerquisites:
  **Disk space**: requires about 100GB disk space.
  **Memory**: The default database size is 29 GB (as of Jan. 2018), and you will need slightly more than that in RAM if you want to build the default database.
  **Dependencies**: It mostly uses Linux commands. Scripts are written mostly in bash shell, and perl. Downloads of NCBI data are performed by wget and rsync.
    Kraken 2 will attempt to use the dustmasker or segmasker programs provided as part of NCBI's BLAST suite to mask low-complexity regions. 

