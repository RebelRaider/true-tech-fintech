import styles from './MobileVersion.module.css';
import Ding from '../../assets/Ding.svg'
import Badge from '../../assets/Badge.svg'
import Button from '../../assets/Button.svg'
import Search from '../../assets/Search.svg'
import Plus from '../../assets/Plus.svg'
import PlusCircle from '../../assets/Plus circle.svg'
import MTSCard from '../../assets/Card MTS Bank.svg'
import Euro from '../../assets/Euro.svg'
import USA from '../../assets/USA.svg'
import Cell from '../../assets/cell.svg'
import Cell1 from '../../assets/cell1.svg'
import Cell2 from '../../assets/Cell2.svg'
import Cell3 from '../../assets/Cell3.svg'
import Cell4 from '../../assets/Cell4.svg'
import {Link} from "react-router-dom";

const MobileVersion = () => {
    return (
        <div className={styles.MainContainer}>
            <div className={styles.SectorContainer}>
                <div className={styles.HeaderContainer}>
                    <div className={styles.icons}>
                        <div>
                            <img src={Ding}/>
                            <img src={Button}/>
                            <img src={Search}/>
                        </div>
                        <div>
                            <img src={Badge}/>
                        </div>
                    </div>
                </div>
                <div className={styles.BodyContainer}>
                    <div className={styles.Counts}>
                        <img src={Plus} width={30} height={30} />
                        <div className={styles.BigText}>Нет счетов на оплату</div>
                    </div>
                    <div className={styles.Money}>
                        <div className={styles.BorderContainer}>
                            <div className={styles.TextDecoration}>Всего средств</div>
                            <div className={styles.TextDecorationBig}>400 000 Р</div>
                        </div>
                        <div className={styles.BorderContainer}>
                            <div className={styles.TextDecoration}>Расходы за май</div>
                            <div className={styles.TextDecorationBig}>0 Р</div>
                        </div>
                    </div>
                    <div className={styles.Cards}>
                        <div className={styles.CardContainer}>
                            <div className={styles.TextForCard}>Карты</div>
                            <img className={styles.Plus} src={PlusCircle}/>
                        </div>
                        <div className={styles.CardContainer}>
                            <div className={styles.TextContainer}>
                                <div>Моя карта</div><p>400 000 Р</p>
                            </div>
                            <img src={MTSCard}/>
                        </div>
                        <div className={styles.Cash}>
                            <div>Мой кошелёк</div>
                            <p>0 Р</p>
                        </div>
                    </div>
                    <div className={styles.PhoneNumberBorder}>
                        <div className={styles.Conteinder}>
                            <div className={styles.TextNumber}>Мой телефон</div>
                            <div className={styles.TextDecor}>МТС +7 ХХХ-ХХХ-ХХ-ХХ</div>
                        </div>
                        <div className={styles.TextNumber}>
                            30,65 Р
                        </div>
                    </div>
                    <div className={styles.EuroContainer}>
                        <div className={styles.Valut}>
                            <div className={styles.TextDecor}>Валюта</div>
                            <div className={styles.EuroUSA}>
                                <img src={USA} width={24}/>
                                <div>USD</div>
                            </div>
                            <div className={styles.EuroUSA}>
                                <img src={Euro} width={24}/>
                                <div>EUR</div>
                            </div>
                        </div>
                        <div className={styles.ValutDeneg}>
                            <div className={styles.TextDecor}>Продать</div>
                            <div className={styles.EuroUSA}>
                                <div>30,00</div>
                            </div>
                            <div className={styles.EuroUSA}>
                                <div>40,00</div>
                            </div>
                        </div>
                        <div className={styles.ValutDeneg}>
                            <div className={styles.TextDecor}>Купить</div>
                            <div className={styles.EuroUSA}>
                                <div>30,00</div>
                            </div>
                            <div className={styles.EuroUSA}>
                                <div>40,00</div>
                            </div>
                        </div>
                    </div>
                    <div className={styles.ButtonContainer}>
                        <button className={styles.Button}>
                            Открыть новый продукт
                        </button>
                    </div>
                </div>
                <div className={styles.FooterPanel}>
                    <img src={Cell1} width={60} height={60}/>
                    <img src={Cell2} width={60} height={60}/>
                    <Link to={"/chat"}><img src={Cell} width={60} height={60}/></Link>
                    <img src={Cell4} width={60} height={60}/>
                    <img src={Cell3} width={60} height={60}/>
                </div>
            </div>
        </div>
    )
}

export default MobileVersion;