use std :: fs;
use std :: io;
use std::io::Write;
fn main() -> io :: Result<()> {
    let input = fs::read_to_string("input.txt")?;
    output.write_all(input.as_bytes())?;
    Ok(())
}