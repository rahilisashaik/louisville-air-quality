class Utils():
    def compute_normalized_value(measured, min_threshold, max_threshold):
        return (measured - min_threshold) / (max_threshold - min_threshold)
    def ppm_to_mg_monitor(ppm, molar_mass):
        return ((ppm * molar_mass) / 24.45) * 0.00024150000000000002
    
    def parse_coordinates(coord):
        lat, lon = coord.split(" N ")[0], coord.split(" N ")[1].replace(" W", "")
        return float(lat), -float(lon)





