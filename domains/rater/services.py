from sqlalchemy.orm import Session
from .models import Rater
import math

# Calculate totals based on current values
def calculate_rater_totals(rater: Rater):
    
    subtotal = sum(exposure.premium for exposure in rater.exposures)
    # tax_factor = math.prod(tax.factor for tax in rater.taxes) if rater.taxes else 1.0
    # final_total = subtotal # * tax_factor

    rater.subtotal_premium = subtotal
    rater.total_modifiers = 1.15 #tax_factor
    rater.final_premium = subtotal * 1.15
    return rater