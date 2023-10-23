use csv::ReaderBuilder;
use std::error::Error;
use std::fs::File;
use std::io::{BufReader, BufWriter};
use std::time::Instant;

fn process_data(data: &Vec<&str>) -> Vec<String> {
    data.iter()
        .map(|&x| (x.parse::<i32>().unwrap() * 2).to_string())
        .collect()
}

fn main() -> Result<(), Box<dyn Error>> {
    let start_time = Instant::now();

    let input_file = File::open("../input.csv")?;
    let output_file = File::create("output.csv")?;

    let reader = BufReader::new(input_file);
    let mut rdr = ReaderBuilder::new().from_reader(reader);

    let writer = BufWriter::new(&output_file);
    let mut wtr = csv::Writer::from_writer(writer);

    for result in rdr.records() {
        let record = result?;
        let processed_data = process_data(&record.iter().collect());
        wtr.write_record(&processed_data)?;
    }

    let duration = start_time.elapsed();
    println!(
        "Rust script executed in {:.4} seconds.",
        duration.as_secs_f64()
    );

    Ok(())
}
