import './promo.css';

import promoImg from './../../img/promo/promo.jpg';

const Promo = () => {
    return (
        <section className="promo">
            <div className="container">
                <div className="promo__content">
                    <div className="promo__text">
                        <div className="promo__title">
                            НАЧНИ УЧИТЬСЯ ПРЯМО СЕЙЧАС!
                        </div>
                        <div className="promo__desc">
                            Регистрируйся, покупай курс и приступай к обучению.
                        </div>
                        <div className="promo__btn-wrapper">
                            <a href="#!" className="promo__btn">
                                Зарегистрироваться
                            </a>
                        </div>
                    </div>
                    <div className="promo__img">
                        <img src={promoImg} alt="Promo" />
                    </div>
                </div>
            </div>
        </section>
    );
}

export default Promo;