import styles from './Card.module.css';

import pythonImg from './../../img/course/python.jpg';
import javaImg from './../../img/course/java.jpg';
import goImg from './../../img/course/go.jpg';

const Card = () => {
    return (
        <div className={styles.card__list}>
            <div className={styles.card__container}>
                <img className={styles.card__img} src={pythonImg} alt="Python" />
                <div className={styles.card__body}>
                    <div className={styles.card__text}>
                        <div className={styles.card__title}>Python</div>
                        <div className={styles.card__desc}>
                            Программирование на языке Python
                        </div>
                    </div>
                </div>
            </div>
            <div className={styles.card__container}>
                <img className={styles.card__img} src={javaImg} alt="Java" />
                <div className={styles.card__body}>
                    <div className={styles.card__text}>
                        <div className={styles.card__title}>Java</div>
                        <div className={styles.card__desc}>
                            Программирование на языке Java
                        </div>
                    </div>
                </div>
            </div>
            <div className={styles.card__container}>
                <img className={styles.card__img} src={goImg} alt="Go" />
                <div className={styles.card__body}>
                    <div className={styles.card__text}>
                        <div className={styles.card__title}>Go</div>
                        <div className={styles.card__desc}>
                            Программирование на языке Go
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Card;