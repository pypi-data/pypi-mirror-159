curl -sSf https://sh.rustup.rs | sh -s -- -y --default-toolchain stable
source ~/.cargo/env
rustup target add armv7-unknown-linux-gnueabihf
maturin build -i python --release --out dist --target armv7-unknown-linux-gnueabihf --manylinux 2014

