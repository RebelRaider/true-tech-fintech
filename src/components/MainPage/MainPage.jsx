import styles from './MainPage.module.css'
import mtsLogo from '../../assets/mts_logo.png'

const MainPage = () => {
    return (
        <main role="main" className={styles.MainContainer} aria-label="Главная страница">
            <div className={styles.HeaderPadding}></div>
            <header className={styles.HeaderContainer}>
                <img src={mtsLogo} width={154} height={40} className={styles.ImgStyle}></img>
                <p className={styles.HeaderFontStyle}>Главная</p>
                <p className={styles.HeaderFontStyle}>Платежи</p>
                <p className={styles.HeaderFontStyle}>История</p>
                <p className={styles.HeaderFontStyle}>Банковские продукты</p>
                <p className={styles.HeaderFontStyle}>Предложения</p>
            </header>
            <div className={styles.BodyContainer}>
                <section className={styles.LeftBar}>
                    <div className={styles.PhoneBar}>
                        <div className={styles.UpperCaseText}>Мой телефон</div>
                        <div>+7 988 899 98 74</div>
                    </div>
                    <div className={styles.CardBar}>
                        <div>Карты</div>
                        <div>МИР*4725 *</div>
                        <div>**** **** **** 4725</div>
                        <div>Мой кошелек</div>
                        <div>100 000 Р</div>
                        <div>Привязать карту другого банка</div>
                    </div>
                    <div className={styles.DepositBar}>
                        <div>Счета</div>
                        <div>Открыть счет до 15% годовых</div>
                    </div>
                    <div className={styles.CreditBar}>
                        <div>Кредиты</div>
                        <div>Оформить заявку на кредит по выгодным ставка за 5 минут</div>
                    </div>
                    <div className={styles.NewProductButton}>
                        <button>Открыть новый продукт</button>
                    </div>
                </section>
                <section>
                Правая часть
                </section>
            </div>
            <footer>

            </footer>
        </main>
    )
}

export default MainPage