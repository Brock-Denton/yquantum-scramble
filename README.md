# yquantum-scramble
tl;dr: A system to verify quantum random number generators' outputs (QRNGs) and keep track of the machine they were produced from.

# Background
We are working towards the DoraHacks challenge of classifying QRNGs by their outputs.

(TODO)
- talk about 

# Components
Our workflow for securely generating and storing high-quality random numbers encompasses the following components:
- generate our own random numbers using DI-QRNG with the CSHS game method
- verify that those numbers satisfy certain sufficient properties of randomness, using NIST software
- calculate the CSHS scores and entanglement fidelities of our QRNGs
- if we have new samples, classify them by what machine they came from (using the fact that decoherence
changes the statistical properties of QRNGs' output)
- tag the samples with the device they originated from, and log these numbers in a blockchain

One could imagine many quantum computers representing different architectures (e.g. superconducting transmon, trapped ion) contributing downtime to produce
high-quality random numbers for cryptography applications. With a blockchain tracking the origins of these sources, if one device or architecture or
DI-QRNG implementation is found to be faulty, it could easily be removed from high-stakes programs.