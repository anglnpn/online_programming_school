//импорт шапки
import Header from '../header/Header.jsx';
//импорт промо
import Promo from '../promo/Promo.jsx';
//импорт рекламы
import Advert from '../advert/Advert.jsx';

function Home () {
    return (
        <div className="home">
            <Header />
            <Promo />
            <Advert />
        </div>
    )
}

export default Home;