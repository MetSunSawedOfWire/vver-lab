from dataclasses import dataclass


@dataclass(kw_only=True, frozen=True, slots=True)
class NuclideData:
    name: str
    sigma_a: float
    sigma_f: float
    nu: float

    def macro_sigma_a(self, concentration: float) -> float:
        if concentration < 0:
            raise ValueError("Концентрация не может быть отрицательной")
        return concentration * self.sigma_a * 1e-24

    def macro_sigma_f(self, concentration: float) -> float:
        if concentration < 0:
            raise ValueError("Концентрация не может быть отрицательной")
        return concentration * self.sigma_f * 1e-24


NUCLEAR_DATA: dict[str, NuclideData] = {
    "U-235": NuclideData(
        name="U-235",
        sigma_a=683.0,
        sigma_f=585.0,
        nu=2.43,
    ),
    "U-238": NuclideData(
        name="U-238",
        sigma_a=2.7,
        sigma_f=0.0,
        nu=0.0,
    ),
    "H-1": NuclideData(
        name="H-1",
        sigma_a=0.332,
        sigma_f=0.0,
        nu=0.0,
    ),
    "B-10": NuclideData(
        name="B-10",
        sigma_a=3840.0,
        sigma_f=0.0,
        nu=0.0,
    ),
}


if __name__ == "__main__":
    u235 = NUCLEAR_DATA["U-235"]
    print(u235)

    sigma_macro_a = u235.macro_sigma_a(concentration=1e21)
    sigma_macro_f = u235.macro_sigma_f(concentration=1e21)
    print(f"Макросечение поглощения: {sigma_macro_a:.4f} см^-1")
    print(f"Макросечение деления: {sigma_macro_f:.4f} см^-1")
