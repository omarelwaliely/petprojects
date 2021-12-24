document.addEventListener('DOMContentLoaded', () => {
    const cardArr = [
        {
            name: 'butterfly',
            image: 'Images/butterfly.jpeg'
        },
        {
            name: 'butterfly',
            image: 'Images/butterfly.jpeg'
        },
        {
            name: 'car',
            image: 'Images/car.jpeg'
        },
        {
            name: 'car',
            image: 'Images/car.jpeg'
        },
        {
            name: 'cat',
            image: 'Images/cat.jpeg'
        },
        {
            name: 'cat',
            image: 'Images/cat.jpeg'
        },
        {
            name: 'chik',
            image: 'Images/chik.jpeg'
        },
        {
            name: 'chik',
            image: 'Images/chik.jpeg'
        },
        {
            name: 'deet',
            image: 'Images/deet.jpeg'
        },
        {
            name: 'deet',
            image: 'Images/deet.jpeg'
        },
        {
            name: 'flower',
            image: 'Images/flower.jpeg'
        },
        {
            name: 'flower',
            image: 'Images/flower.jpeg'
        },
        {
            name: 'food',
            image: 'Images/food.jpeg'
        },
        {
            name: 'food',
            image: 'Images/food.jpeg'
        },
        {
            name: 'helicopter',
            image: 'Images/helicopter.jpeg'
        },
        {
            name: 'helicopter',
            image: 'Images/helicopter.jpeg'
        },
        {
            name: 'tree',
            image: 'Images/tree.jpeg'
        },
        {
            name: 'tree',
            image: 'Images/tree.jpeg'
        },
        {
            name: 'universe',
            image: 'Images/universe.jpeg'
        },
        {
            name: 'universe',
            image: 'Images/universe.jpeg'
        },
        {
            name: 'waterfall',
            image: 'Images/waterfall.jpeg'
        },
        {
            name: 'waterfall',
            image: 'Images/waterfall.jpeg'
        },
        {
            name: 'wolf',
            image: 'Images/wolf.jpeg'
        },
        {
            name: 'wolf',
            image: 'Images/wolf.jpeg'
        }

    ]

    cardArr.sort(() => 0.5 - Math.random())

    const grid = document.querySelector('.grid')
    const resultDisplay = document.querySelector('#result')
    let cardsChosen = []
    let cardsChosenId = []
    let cardsWon = []

    function createBoard() {
        for (let i = 0; i < cardArr.length; i++) {
            const card = document.createElement('img')
            card.setAttribute('src', 'Images/blank.jpeg')
            card.setAttribute('data-id', i)
            card.addEventListener('click', flipCard)
            grid.appendChild(card)
        }
    }
    function checkForMatch() {
        const cards = document.querySelectorAll('img')
        const optionOneId = cardsChosenId[0]
        const optionTwoId = cardsChosenId[1]

        if (optionOneId == optionTwoId) {
            cards[optionOneId].setAttribute('src', 'Images/blank.jpeg')
            cards[optionTwoId].setAttribute('src', 'Images/blank.jpeg')
        }
        else if (cardsChosen[0] === cardsChosen[1]) {
            cards[optionOneId].setAttribute('src', 'Images/refresh.jpeg')
            cards[optionTwoId].setAttribute('src', 'Images/refresh.jpeg')
            cards[optionOneId].removeEventListener('click', flipCard)
            cards[optionTwoId].removeEventListener('click', flipCard)
            cardsWon.push(cardsChosen)
        } else {
            cards[optionOneId].setAttribute('src', 'Images/blank.jpeg')
            cards[optionTwoId].setAttribute('src', 'Images/blank.jpeg')
        }
        cardsChosen = []
        cardsChosenId = []
        resultDisplay.textContent = cardsWon.length * 100
        if (cardsWon.length === cardArr.length / 2) {
            resultDisplay.textContent = 'You Won!'
        }
    }

    function flipCard() {
        let cardId = this.getAttribute('data-id')
        cardsChosen.push(cardArr[cardId].name)
        cardsChosenId.push(cardId)
        this.setAttribute('src', cardArr[cardId].image)
        if (cardsChosen.length === 2) {
            setTimeout(checkForMatch, 200)
        }
    }
    createBoard()
})