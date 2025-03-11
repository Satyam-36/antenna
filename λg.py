import math

def calculate_lambda_g():
    # Taking user inputs
    c = 3e8  # Speed of light in m/s
    f_r = float(input("Enter the resonant frequency in GHz: ")) * 1e9  # Convert GHz to Hz
    epsilon_r = float(input("Enter the relative permittivity (εr) of the substrate: "))
    h = float(input("Enter the substrate thickness in mm: ")) * 1e-3  # Convert mm to meters
    W = float(input("Enter the patch width in mm: ")) * 1e-3  # Convert mm to meters
    
    # Calculate free-space wavelength
    lambda_0 = c / f_r
    
    # Calculate effective permittivity
    epsilon_eff = (epsilon_r + 1) / 2 + (epsilon_r - 1) / 2 * (1 + 12 * (h / W)) ** -0.5
    
    # Calculate guided wavelength
    lambda_g = lambda_0 / math.sqrt(epsilon_eff)
    
    # Convert result back to mm for better readability
    print(f"\nResults:")
    print(f"Free-space Wavelength (λ0) = {lambda_0 * 1e3:.2f} mm")
    print(f"Effective Permittivity (εeff) = {epsilon_eff:.2f}")
    print(f"Guided Wavelength (λg) = {lambda_g * 1e3:.2f} mm")

# Run the function
calculate_lambda_g()
