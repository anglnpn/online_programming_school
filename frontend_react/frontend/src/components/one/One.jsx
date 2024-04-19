//импорт шапки
import Header from '../header/Header.jsx';
//импорт промо
import Promo from '../promo/Promo.jsx';
//импорт рекламы
import Advert from '../advert/Advert.jsx';

import Footer from '../info_form/InfoForm.jsx';

function Home () {
    return (
        <div className="home">
            <Header />
            <Promo />
            <Advert />
            <Footer />
        </div>
    )
}

export default Home;