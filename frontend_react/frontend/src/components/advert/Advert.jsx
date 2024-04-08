import './advert.css';

import Card from '../advert_card/Card.jsx';

const Advert = () => {
    return (
        <section className="advert">
            <div className="container">
                <div className="advert__header">
                    <div className="title__2">
                        НAШИ КУРСЫ
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