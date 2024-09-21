import numpy as np
import re


def convert_to_numeric(value):
        if isinstance(value, str):
            # Handle ranges like '3.50-3' or '3.00 - 2.50'
            match = re.findall(r"\d+\.\d+|\d+", value)
            if len(match) == 2:
                return (float(match[0]) + float(match[1])) / 2
            elif len(match) == 1:
                return float(match[0])
            elif "altı" in value in value:  # handle '2.50 ve altı' and 'hazırlığım'
                return float(2.50)  # Use a code to represent such cases
            elif "ortalama bulunmuyor" in value or "not ortalaması yok" in value or 'hazırlığım' in value:
                return np.nan  # Handle missing or unavailable data
        return np.nan

if __name__ == "__main__":
    print(convert_to_numeric('3.50-3'))
    print(convert_to_numeric('3.00 - 2.50'))
    print(convert_to_numeric('3.50'))
    print(convert_to_numeric('2.50 ve altı'))
    print(convert_to_numeric('ortalama bulunmuyor'))
    print(convert_to_numeric('not ortalaması yok'))
    print(convert_to_numeric('hazırlığım'))