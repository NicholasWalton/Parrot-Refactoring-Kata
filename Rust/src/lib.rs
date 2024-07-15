struct Parrot {
    parrot_type: ParrotType,
    number_of_coconuts: usize,
    voltage: f32,
    nailed: bool,
}

enum ParrotType {
    European,
    African,
    NorwegianBlue,
}

impl Default for Parrot {
    fn default() -> Self {
        Parrot {
            parrot_type: ParrotType::European,
            number_of_coconuts: 0,
            voltage: 0.0,
            nailed: false
        }
    }
}

impl Parrot {
    pub fn speed(&self) -> Result<f32, &'static str> {
        match self.parrot_type {
            ParrotType::European => Ok(base_speed()),
            ParrotType::African => {
                let african_speed = base_speed() - load_factor() * self.number_of_coconuts as f32;
                if african_speed > 0.0 { Ok(african_speed) } else { Ok(0.0)}
            }
            ParrotType::NorwegianBlue => {
                if self.nailed == true {
                    Ok(0.0)
                }
                else {
                    Ok(compute_base_speed_for_voltage(self.voltage))
                }
            }
        }
    }

    pub(crate) fn get_cry(&self) -> Result<&str, &'static str> {
        match self.parrot_type {
            ParrotType::European => Ok("Sqoork!"),
            ParrotType::African => Ok("Sqaark!"),
            ParrotType::NorwegianBlue => if self.voltage > 0.0 { Ok("Bzzzzzz") } else { Ok("...") },
        }
    }
}

fn compute_base_speed_for_voltage(voltage: f32) -> f32 {
    let fixed_base_speed = 24.0;
    let base_speed_for_voltage = voltage * base_speed();
    if base_speed_for_voltage < fixed_base_speed {
        base_speed_for_voltage
    }
    else {
        fixed_base_speed
    }
}

fn load_factor() -> f32 {
    9.0
}

fn base_speed() -> f32 {
    12.0
}

#[cfg(test)]
mod tests {
    use std::default;

    use super::*;

    #[test]
    fn european_parrot_speed() {
        let parrot = Parrot::default();
        assert_eq!(parrot.speed().unwrap(), 12.0);
    }

    #[test]
    fn african_parrot_speed_with_one_coconut() {
        let parrot = Parrot { parrot_type: ParrotType::African,
                              number_of_coconuts: 1,
                              ..Default::default() 
                            };
        assert_eq!(parrot.speed().unwrap(), 3.0);
    }

    #[test]
    fn african_parrot_speed_with_two_coconut() {
        let parrot = Parrot { parrot_type: ParrotType::African,
                              number_of_coconuts: 2,
                              ..Default::default()
                            };
        assert_eq!(parrot.speed().unwrap(), 0.0);
    }

    #[test]
    fn african_parrot_speed_with_no_coconut() {
        let parrot = Parrot { parrot_type: ParrotType::African,
                              ..Default::default()
                            };
        assert_eq!(parrot.speed().unwrap(), 12.0);
    }
    #[test]
    fn nailed_norwegian_blue_parrot() {
        let parrot = Parrot { parrot_type: ParrotType::NorwegianBlue,
                              voltage: 1.5,
                              nailed: true,
                            ..Default::default()
                        };
        assert_eq!(parrot.speed().unwrap(), 0.0);
    }
    #[test]
    fn not_nailed_norwegian_blue_parrot() {
        let parrot = Parrot { parrot_type: ParrotType::NorwegianBlue,
                              voltage: 1.5,
                              ..Default::default()
                            };
        assert_eq!(parrot.speed().unwrap(), 18.0);
    }
    #[test]
    fn not_nailed_norwegian_blue_parrot_with_high_voltage() {
        let parrot = Parrot { parrot_type: ParrotType::NorwegianBlue,
                              voltage: 4.0,
                            ..Default::default() };
        assert_eq!(parrot.speed().unwrap(), 24.0);
    }

    #[test]
    fn get_cry_of_european_parrot()
    {
        let parrot = Parrot::default();
        assert_eq!(parrot.get_cry().unwrap(), "Sqoork!");
    }

    #[test]
    fn get_cry_of_african_parrot()
    {
        let parrot = Parrot {
            parrot_type: ParrotType::African,
            ..Default::default()
        };
        assert_eq!(parrot.get_cry().unwrap(), "Sqaark!");
    }

    #[test]
    fn get_cry_norwegian_blue_parrot_high_voltage()
    {
        let parrot = Parrot {
            parrot_type: ParrotType::NorwegianBlue,
            voltage: 4.0,
            ..Default::default()
        };
        assert_eq!(parrot.get_cry().unwrap(), "Bzzzzzz");
    }

    #[test]
    fn get_cry_norwegian_blue_parrot_no_voltage()
    {
        let parrot = Parrot {
            parrot_type: ParrotType::NorwegianBlue,
            ..Default::default()
        };
        assert_eq!(parrot.get_cry().unwrap(), "...");
    }
}
