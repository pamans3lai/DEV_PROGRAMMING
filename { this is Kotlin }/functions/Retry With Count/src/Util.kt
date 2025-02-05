import java.math.BigDecimal
import kotlin.random.Random

class Account(
    val iban: String,
    val product: String,
    val currency: String,
    val balance: BigDecimal
) {
    init {
        require(currency.length == 3) { "Currency should be a 3 chars code" }
        require(iban.matches("[A-Z]{2}\\d{2}[A-Z]{4}\\d{16}".toRegex())) { "Invalid IBAN" }
    }
}

fun Account.deposit(amount: BigDecimal): Account = Account(
    iban,
    product,
    currency,
    balance = balance + amount
)

fun fail(probability: Int) = check(Random.nextInt(100) > probability) {
    "simulated side effect exception"
}
