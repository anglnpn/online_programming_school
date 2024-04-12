import './advert.css';

import Card from '../advert_card/Card.jsx';

const Advert = () => {
    return (
        <section className="advert">
            <div className="container">
                <div className="advert__header">
                    <div className="title__2">
                        ПОСЛЕ РЕГИСТРАЦИИ ТЫ ПОЛУЧИШЬ ДОСТУП К БОЛЬШОМУ КОЛИЧЕСТВУ КУРСОВ!

                    <div className="title__3"> ВОТ САМЫЕ ПОПУЛЯРНЫЕ:</div>
                    </div>
                </div>
                <div className="advert__card">
                    <Card />
                </div>
            </div>

        </section>
    );
}

export default Advert;