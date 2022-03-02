from django.shortcuts import render
import random
from json import dumps
# Create your views here.

def home(request):
    try:
        content={
                    "tg":request.session['total_games'],
                    "th":request.session['total_head'],
                    "tt":request.session['total_tail'],
                    "tp":request.session['total_payout'],
                    "tr":request.session['total_reverse'],
                    "gc":request.session['guess_coin'],
                    "ba":request.session['bet_amount'] ,
                    "gr":request.session['game_result'],
                    "jp":request.session['jackpot'],
            }
    except:
        request.session['total_games'] =0
        request.session['total_head'] =0
        request.session['total_tail'] =0
        request.session['total_payout']  =0
        request.session['total_reverse'] =0
        request.session['jackpot']=0
        content={
                    "tg":request.session['total_games'],
                    "th":request.session['total_head'],
                    "tt":request.session['total_tail'],
                    "tp":request.session['total_payout'],
                    "tr":request.session['total_reverse'],
                    "gc":"n/a",
                    "ba":"n/a" ,
                    "gr":"n/a",
                    "jp":request.session['jackpot'],
            }
    return render( request, 'index.html',content )

def flip(request):
        bet_amount= request.session['bet_amount']
        guess_coin=request.session['guess_coin']
        game_result,coin_result,bet_amount=flipcoin(bet_amount,guess_coin)
      
        request.session['game_result'] =game_result
        if  request.session.get('total_games'):
            tg=request.session['total_games']
            th=request.session['total_head']
            tt=request.session['total_tail']
            tp=request.session['total_payout'] 
            tr=request.session['total_reverse']
            request.session['total_games']=int(tg)+1
            if  coin_result=="Head":
                request.session['total_head']=int(th)+1
            else:
                request.session['total_tail']=int(tt)+1
            request.session['total_payout']=int(tp)+int(bet_amount)
            if  game_result=="Win":
                request.session['total_reverse']=int(tr)+int(bet_amount)
                result_promt='Congratulations,You win '+str(bet_amount)+'$'
   
            else:
                result_promt='Sorry You Lose.Better Luck Next Time'
      
        else:
            request.session['total_games'] =0
            request.session['total_head'] =0
            request.session['total_tail'] =0
            request.session['total_payout']  =0
            request.session['total_reverse'] =0
            tg=request.session['total_games']
            th=request.session['total_head']
            tt=request.session['total_tail']
            tp=request.session['total_payout'] 
            tr=request.session['total_reverse']
            request.session['total_games']=int(tg)+1
            if  coin_result=="Head":
                request.session['total_head']=int(th)+1
            else:
                request.session['total_tail']=int(tt)+1
            request.session['total_payout']=int(tp)+int(bet_amount)
            if  game_result=="Win":
                request.session['total_reverse']=int(tr)+int(bet_amount)
                result_promt='Congratulations,You win '+str(bet_amount)+'$'
   
            else:
                result_promt='Sorry You Lose.Better Luck Next Time'
       
        if True: 
            if lastDigit(int(request.session['total_payout'])):
                request.session['jackpot']=int(request.session['jackpot'])+int(request.session['total_payout'])+10
                result_promt = result_promt + " Congratulations,You win A Jackpot"
        else:
            request.session['jackpot']=0
        content={
            "tg":request.session['total_games'],
            "th":request.session['total_head'],
            "tt":request.session['total_tail'],
            "tp":request.session['total_payout'],
            "tr":request.session['total_reverse'],
            "gc":request.session['guess_coin'],
            "ba":request.session['bet_amount'] ,
            "gr":request.session['game_result'],
            "jp":request.session['jackpot'],
            "message":result_promt,
        }
        return render( request, 'index.html',content )

def flipcoin(bet_amount,guess_coin):
    num=random.randint(1,2)
    if num==1:
        coin_result="Head"
    elif num==2:
        coin_result="Tail"

    if coin_result == guess_coin:
        game_result="Win"
        return game_result,coin_result,bet_amount,
    else:
        game_result="Lose"
        return game_result,coin_result,bet_amount,


def payment(request):
    if request.method == 'POST':
        bet_amount=request.POST.get('payment_amount', False)
        guess_coin=request.POST.get('coinside', False)
        request.session['guess_coin'] =guess_coin
        request.session['bet_amount'] =bet_amount
        content={
            "amount":bet_amount,
        }
        return render( request, 'index2.html' ,content)




def coinflip(request):
    content={
            "jp":request.session['jackpot'],
       
        }
    return render( request, 'coinflipp.html',content )


def lastDigit(n) :
    
    last_digit=int(n%10)
    second_last_digit=int((n % 100)/10)
    temp = str(last_digit)+ str(second_last_digit)
    if temp == "99":
        return True
    else:
        return False