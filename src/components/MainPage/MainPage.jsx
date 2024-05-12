import styles from './MainPage.module.css'
import mtsLogo from '../../assets/mts_logo.png'
import AddButton from '../../assets/AddButton.svg'
import CardMTS from '../../assets/Card MTS Bank.svg'

const MainPage = () => {
    return (
        <main role="main" className={styles.MainContainer} aria-label="Главная страница">
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
                        <div className={styles.CaseText}>+7 988 899 98 74</div>
                    </div>
                    <div className={styles.CardBar}>
                        <div className={styles.UpperCaseTextCard}>Карты</div>
                        <div className={styles.CaseText}>МИР*4725</div>
                        <div className={styles.CaseTextNumber}>**** **** **** <div className={styles.Up}>4725</div><img className={styles.imgStyle} src={CardMTS}/></div>
                        <div className={styles.CaseText}>Мой кошелек</div>
                        <div className={styles.CaseTextNumber}><div className={styles.Up}>400 000 Р</div></div>
                        <div className={styles.CaseText}>Привязать карту другого банка</div>
                    </div>
                    <div className={styles.DepositBar}>
                        <div className={styles.UpperCaseTextCard}>Счета</div>
                        <div className={styles.AddButtonContainer}>
                            <div className={styles.CaseTextButton}>Открыть счет до 15% годовых</div>
                            <img src={AddButton} width={46} height={46}/>
                        </div>
                    </div>
                    <div className={styles.CreditBar}>
                        <div className={styles.UpperCaseTextCardButton}>Кредиты</div>
                        <div className={styles.AddButtonContainer}>
                            <div className={styles.CaseTextButton}>Оформить заявку<br/>на кредит по выгодным ставкам за 5 минут</div>
                            <img src={AddButton} width={46} height={46}/>
                        </div>
                    </div>
                    <div className={styles.NewProductButton}>
                        <button className={styles.Button}>Открыть новый продукт</button>
                    </div>
                </section>
                <section className={styles.RightBar}>
                    <div className={styles.Templates}>
                        <div className={styles.TemplatesUp}>Шаблоны и автоплатежи</div>
                        <div className={styles.BottomTemplate}>
                            <div className={styles.Card}>
                                <div className={styles.Circle}></div>
                                <div className={styles.TextOnCard}>Счета на оплату</div>
                            </div>
                            <div className={styles.Card}>
                                <div className={styles.Circle}></div>
                                <div className={styles.TextOnCard}>Шаблоны</div>
                            </div>
                            <div className={styles.Card}>
                                <div className={styles.Circle}></div>
                                <div className={styles.TextOnCard}>Автоплатежи</div>
                            </div>
                            <div className={styles.Card}>
                                <div className={styles.Circle}></div>
                                <div className={styles.TextOnCard}>Создать новый</div>
                            </div>
                        </div>
                    </div>
                    <div className={styles.CashBack}>
                        <div className={styles.TemplatesUp}>Кешбэк</div>
                        <div className={styles.BottomTemplate}>
                            <div className={styles.CashBackBorder}>
                                <div className={styles.MTSCachBack}>MTS Cashback</div>
                            </div>
                        </div>
                    </div>
                    <div className={styles.More}>
                        <div className={styles.TemplatesUp}>Еще</div>
                        <div className={styles.BottomTemplate}>
                            <div className={styles.Card}>
                                <div className={styles.Circle}></div>
                                <div className={styles.TextOnCard}>Счета на оплату</div>
                            </div>
                            <div className={styles.Card}>
                                <div className={styles.Circle}></div>
                                <div className={styles.TextOnCard}>Комиссии и лимиты</div>
                            </div>
                            <div className={styles.Card}>
                                <div className={styles.Circle}></div>
                                <div className={styles.TextOnCard}>Справки и выписки</div>
                            </div>
                            <div className={styles.Card}>
                                <div className={styles.Circle}></div>
                                <div className={styles.TextOnCard}>Офисы и банкоматы</div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>
            <footer>
            </footer>
        </main>
    )
}

export default MainPage;