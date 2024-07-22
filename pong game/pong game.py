import pygame
from sys import exit
from random import choice
import time

pygame.init()

screen_width=1280
screen_height=716
screen=pygame.display.set_mode((screen_width,screen_height),pygame.RESIZABLE)
pygame.display.set_caption("PONG")

bground=pygame.image.load("image/pong_back.jpg")
pong_icon=pygame.image.load("image/pong_icon.png")
pygame.display.set_icon(pong_icon)

ball=pygame.Rect(screen_width/2 - 15,screen_height/2 - 15,30,30)
player1=pygame.Rect(20,screen_height/2 - 70,10,140)
player2=pygame.Rect(screen_width - 20,screen_height/2 - 70,10,140)

bg_color=pygame.Color("grey12")
light_grey=(200,200,200)

clock=pygame.time.Clock()
ball_speed_x=4*choice((1,-1))
ball_speed_y=4*choice((1,-1))
def ball_anime():
    global ball_speed_x,ball_speed_y,player1_score,player2_score,score_time
    ball.x+=ball_speed_x
    ball.y+=ball_speed_y
    if ball.top<=0 or ball.bottom>=screen_height:
        ball_speed_y*=-1
        pong_sound.play()
    
    if ball.left<=0 or ball.right>=screen_width:
        if ball.left<=0:
            player2_score+=1
        if ball.right>=screen_width:
            player1_score+=1
        score_sound.play()
        score_time=pygame.time.get_ticks()
        ball.center=(screen_width/2,screen_height/2)
        player1.x,player1.y=20,screen_height/2-70
        player2.x,player2.y=screen_width-20,screen_height/2-70
        ball_speed_x=4*choice((1,-1))
        ball_speed_y=4*choice((1,-1))

        
    if ball.colliderect(player1) and ball_speed_x<0:
        pong_sound.play()
        if abs(ball.left-player1.right)<10:
            ball_speed_x*=-1
            
        elif abs(ball.bottom-player1.top)<10 and ball_speed_y>0:
            ball_speed_y*=-1
            
        elif abs(ball.top-player1.bottom)<10 and ball_speed_y<0:
            ball_speed_y*=-1
            
    if ball.colliderect(player2) and ball_speed_x>0:
        pong_sound.play()
        if abs(ball.right-player2.left)<10:
            ball_speed_x*=-1
        
        elif abs(ball.bottom-player2.top)<10 and ball_speed_y>0:
            ball_speed_y*=-1
        
        elif abs(ball.top-player2.bottom)<10 and ball_speed_y<0:
            ball_speed_y*=-1

def player_anime(player):

    if player.top<=0:
        player.top=0
        
    if player.bottom>=screen_height:
        player.bottom=screen_height


class Button():
    def __init__(self,text,*color):
        self.text=text
        self.color=color
        self.tap=True
        self.original_color=color
        
        
    def draw(self,left,top,width,height,border_radius,font):
        self.text_surface=font.render(self.text,True,"white")
        self.rect=pygame.Rect(left,top,width,height)
        pygame.draw.rect(screen,self.color,self.rect,0,border_radius)
        self.text_rect=self.text_surface.get_rect(center=self.rect.center)
        screen.blit(self.text_surface,self.text_rect)
        
    def is_clicked(self,event):
        global tap,score_time
        score_time=pygame.time.get_ticks()
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and self.rect.collidepoint(event.pos):
            return True
        if self.tap==True and not self.rect.collidepoint(pygame.mouse.get_pos()):
            self.color=self.original_color
        else:
            self.color="black"
            
        
        

            


player1_speed=0
player2_speed=0
player1_score=0
player2_score=0
win_score=5
winner=""

score_time=pygame.time.get_ticks()
font1=pygame.font.Font("freesansbold.ttf",32)
font2=pygame.font.Font("fonts/Kanit-Bold.ttf",64)
font3=pygame.font.Font("fonts/Kanit-Bold.ttf",128)
font4=pygame.font.Font("fonts/Kanit-Light.ttf",64)


pong_sound=pygame.mixer.Sound("sound/pong.ogg")
score_sound=pygame.mixer.Sound("sound/score.ogg")
click_sound=pygame.mixer.Sound("sound/click.mp3")
losing_sound=pygame.mixer.Sound("sound/losing1.mp3")

bg_music=pygame.mixer.Sound("sound/Slow Burn.mp3")
bg_music.set_volume(0.3)
bg_music.play(-1)
restart_icon=pygame.image.load("image/restart_icon.png")
scaled_restart_icon=pygame.transform.scale(restart_icon,(100,100))
restart_icon_rect=scaled_restart_icon.get_rect(center=(640,500))

up=pygame.image.load("image/up.png")
scaled_up=pygame.transform.scale(up,(100,100))

down=pygame.image.load("image/down.png")
scaled_down=pygame.transform.scale(down,(100,100))

W_button=pygame.image.load("image/W_button.png")
scaled_W=pygame.transform.scale(W_button,(100,100))

S_button=pygame.image.load("image/S_button.png")
scaled_S=pygame.transform.scale(S_button,(100,100))

game_active=1

p_button=Button("2-Players",(50,50,50))
a_button=Button("Computer",(50,50,50))
score_to_win=Button("WINNING SCORE",(0,0,0))
input_bar=Button(f"{win_score}",(100,100,100))

vs_AI=False
input_bar_clicked=False
x=1
size=True

while True:
    current_time=pygame.time.get_ticks()
    
    if game_active==1:
        screen.fill((158,151,143))
        screen.blit(bground,(300,100))
        p_button.draw(900,300,320,100,30,font2)
        a_button.draw(900,500,320,100,30,font2)
        score_to_win.draw(300,450,0,0,0,font2)
        input_bar.draw(200,500,200,50,10,font4)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active==1:
            if p_button.is_clicked(event):
                click_sound.play()
                time.sleep(0.5)
                game_active=2
                vs_AI=False
                
            if a_button.is_clicked(event):
                click_sound.play()
                time.sleep(0.5)
                game_active=2
                vs_AI=True
            
            if input_bar.is_clicked(event):
                input_bar.color=(70,70,70)
                input_bar.tap=False
                input_bar_clicked=True
                
            if input_bar_clicked and event.type==pygame.KEYDOWN:
                
                win_score=str(win_score)
                
                if event.key in range(48,58):
                    win_score+=event.unicode
                if event.key==8 or int(win_score)>99:
                    win_score=win_score[0:len(win_score)-1]
                
                input_bar.text=win_score
    
                if win_score=="":
                    win_score=0
                win_score=int(win_score)
        
        if game_active==2:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    game_active=3
                    size=True
                    x=1
                    score_time=pygame.time.get_ticks()
                    bg_music.stop()
        
        if game_active==3:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    player1_speed+=7
                    
                if event.key==pygame.K_s:
                    player1_speed-=7
                    
                if not vs_AI:
                    if event.key==pygame.K_UP:
                        player2_speed+=7
                        
                    if event.key==pygame.K_DOWN:
                        player2_speed-=7

                        
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_w:
                    player1_speed-=7
                
                if event.key==pygame.K_s:
                    player1_speed+=7
                    
                if not vs_AI:
                    if event.key==pygame.K_UP:
                        player2_speed-=7
                        
                    if event.key==pygame.K_DOWN:
                        player2_speed+=7
                    
        
        if game_active==4:
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and restart_icon_rect.collidepoint(event.pos):
                click_sound.play()
                time.sleep(0.5)
                game_active=1
                input_bar.tap=True
                input_bar_clicked=False
                player1_score=player2_score=0
                player1.centery=player2.centery=screen_height/2
                player1_speed=player2_speed=0
                x=1
                size=True
                bg_music.play(-1)

    diff_time=current_time-score_time

    if game_active==2:
        screen.fill(bg_color)
        pygame.draw.rect(screen,light_grey,player1)
        pygame.draw.rect(screen,light_grey,player2)
        pygame.draw.line(screen,"black",(screen_width/2,0),(screen_width/2,screen_height),10)
        
        screen.blit(scaled_W,(100,280))
        screen.blit(scaled_S,(100,420))
        
        up_text=font4.render("MOVE UP",True,"white")
        down_text=font4.render("MOVE DOWN",True,"white")
        screen.blit(up_text,(220,280))
        screen.blit(down_text,(220,420))
        
        if vs_AI:
            text1=font2.render("YOU",True,"white")
            text2=font2.render("COMPUTER",True,"white")
        else:
            text1=font2.render("PLAYER 1",True,"white")
            text2=font2.render("PLAYER 2",True,"white")
            screen.blit(scaled_up,(740,300))
            screen.blit(scaled_down,(740,400))
            screen.blit(up_text,(860,300))
            screen.blit(down_text,(860,400))
        screen.blit(text1,(200,100))
        screen.blit(text2,(840,100))
    

        
    
        play_text=font2.render("PRESS ENTER TO PLAY",True,"grey")
        scaled_play_text=pygame.transform.scale_by(play_text,x)
        play_text_rect=scaled_play_text.get_rect(center=(640,600))
        screen.blit(scaled_play_text,play_text_rect)
        if size==True:
            x-=0.01
            if x<=0.5:
                size=False
        else:
            x+=0.01
            if x>=1:
                size=True
    
    if game_active==3:      
        player1.y-=player1_speed
        player2.y-=player2_speed
    
        player_anime(player1)
        player_anime(player2)
        
        if vs_AI:
            if ball.centery<player2.centery and player2.top>0:
                player2.centery-=7
            if ball.centery>player2.centery and player2.bottom<screen_height:
                player2.centery+=7
            
        
        screen.fill(bg_color)
        pygame.draw.rect(screen,light_grey,player1)
        pygame.draw.rect(screen,light_grey,player2)
        pygame.draw.line(screen,"black",(screen_width/2,0),(screen_width/2,screen_height),10)
        pygame.draw.ellipse(screen,light_grey,ball)
    
        player1_text=font1.render(f"{player1_score}",True,light_grey)
        screen.blit(player1_text,(600,358))
        
        player2_text=font1.render(f"{player2_score}",True,light_grey)
        screen.blit(player2_text,(660,358))
        
        # print(diff_time)
        if diff_time%10000 in list(range(1,20)):
            if ball_speed_x>0:
                ball_speed_x+=1
            else:
                ball_speed_x-=1
                
            if ball_speed_y>0:
                ball_speed_y+=1
            else:
                ball_speed_y-=1
                
                
        if diff_time>=2100:
            ball_anime()
        else:
            timer_text=font3.render(f"{int((2100-diff_time)/700 + 1)}",True,"white")
            screen.blit(timer_text,(600,550))
            

            
        if player1_score==win_score or player2_score==win_score:
            game_active=4
            losing_sound.play()
        
            
    if game_active==4:
        screen.fill(light_grey)

        if not vs_AI:
            if player1_score==win_score:
                winner="PLAYER 1 WON!"
            if player2_score==win_score:
                winner="PLAYER 2 WON!"
            
        else:
            if player1_score==win_score:
                winner="YOU WON!"
            if player2_score==win_score:
                winner="COMPUTER WON!"
        
        win_text=font3.render(winner,True,"black")
        screen.blit(win_text,(200,80))
        
        restart_text=font4.render("RESTART",True,"black")
        scaled_restart_text=pygame.transform.scale_by(restart_text,x)
        restart_text_rect=scaled_restart_text.get_rect(center=(640,400))
        screen.blit(scaled_restart_text,restart_text_rect)
        screen.blit(scaled_restart_icon,restart_icon_rect)
        if size==True:
            x-=0.01
            if x<=0.5:
                size=False   
        else:
            x+=0.01
            if x>=1:
                size=True
        
    pygame.display.flip()
    clock.tick(60)

