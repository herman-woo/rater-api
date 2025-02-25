from sqlalchemy.orm import Session
from .models import Rater
import math

# Calculate totals based on current values
def calculate_rater_totals(rater: Rater):    
    subtotal = sum(exposure.premium for exposure in rater.exposures)
    modifiers = math.prod(credit.factor for credit in rater.credits) if rater.credits else 1.0

    rater.subtotal_premium = subtotal
    rater.total_modifiers = modifiers
    rater.final_premium = subtotal * modifiers
    return rater