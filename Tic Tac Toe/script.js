agent='X'
player='O'

//creating empty board
let board=new Array(3)
for(var i=0;i<3;i++)
{
    board[i]=new Array(3)
    for(var j=0;j<3;j++)
    board[i][j]=''
}

//getting each cell
cellOne=document.getElementById('one')
cellTwo=document.getElementById('two')
cellThree=document.getElementById('three')
cellFour=document.getElementById('four')
cellFive=document.getElementById('five')
cellSix=document.getElementById('six')
cellSeven=document.getElementById('seven')
cellEight=document.getElementById('eight')
cellNine=document.getElementById('nine')


//adding event listeners
playerTurn=(player)=>{
    if(player.innerHTML=='')
    {
        player.innerHTML='O'
        if(player.id=='one')
        {
            board[0][0]='O'
        }
        else if(player.id=='two')
        {
            board[0][1]='O'
        }
        else if(player.id=='three')
        {
            board[0][2]='O'
        }
        else if(player.id=='four')
        {
            board[1][0]='O'
        }
        else if(player.id=='five')
        {
            board[1][1]='O'
        }
        else if(player.id=='six')
        {
            board[1][2]='O'
        }
        else if(player.id=='seven')
        {
            board[2][0]='O'
        }
        else if(player.id=='eight')
        {
            board[2][1]='O'
        }
        else
        {
            board[2][2]='O'
        }
        checkWinner()
    }
}


cellOne.addEventListener('click',()=>{
    playerTurn(cellOne)
})
cellTwo.addEventListener('click',()=>{
    playerTurn(cellTwo)
})
cellThree.addEventListener('click',()=>{
    playerTurn(cellThree)
})
cellFour.addEventListener('click',()=>{
    playerTurn(cellFour)
})
cellFive.addEventListener('click',()=>{
    playerTurn(cellFive)
})
cellSix.addEventListener('click',()=>{
    playerTurn(cellSix)
})
cellSeven.addEventListener('click',()=>{
    playerTurn(cellSeven)
})
cellEight.addEventListener('click',()=>{
    playerTurn(cellEight)
})
cellNine.addEventListener('click',()=>{
    playerTurn(cellNine)
})



//utility function
checkWinner=()=>{

}


makeMove=()=>{

}


//main algorithm
genScore=()=>{

}

minimax=()=>{
    
}