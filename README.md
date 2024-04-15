# yquantum-scramble

**yquantum-scramble** is an innovative system designed to verify the outputs of quantum random number generators (QRNGs) and maintain a record of the machines that produced these outputs. This project aligns with our efforts to contribute to the DoraHacks challenge, focusing on classifying QRNGs by analyzing their output characteristics.

## Background

Quantum random number generators (QRNGs) are pivotal in various applications ranging from cryptography to scientific simulations.

## Components

Our solution comprises several critical components that collectively ensure the reliability and efficacy of quantum-generated randomness:
- Random Number Generation: We generate our own random numbers utilizing Device-Independent Quantum Random Number Generation (DI-QRNG) based on the Clauser-Horne-Shimony-Holt (CHSH) game method.
- Randomness Verification: Verification of the randomness of numbers is done using the NIST Statistical Test Suite, ensuring they meet the established randomness criteria.
- Quantum Evaluation Metrics: We compute CHSH scores and entanglement fidelities to evaluate the performance of our QRNGs.
- Machine Classification: Newly generated samples are classified according to the quantum machine of origin.
- Blockchain Logging: Each batch of random numbers is tagged with its origin device and securely logged in a blockchain.

## Getting Started

"To set up `yquantum-scramble` on your local machine for development and testing purposes, follow these steps:

1. Clone the repository:
   'git clone https://github.com/your-organization/yquantum-scramble.git'

2. Navigate to the project directory:
   'cd yquantum-scramble'

3. Install the required dependencies:
   'pip install -r requirements.txt'"

## Usage

To start using `yquantum-scramble`, run the following command:
'python main.py'
This script will initiate the QRNG process, perform validation checks, and log the data to the blockchain.

## Contributing

We welcome contributions from the community. If you wish to contribute to `yquantum-scramble`, please fork the repository and submit a pull request. For substantial changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
