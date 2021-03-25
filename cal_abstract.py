#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on Wed Mar 24 21:35:31 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.4'
expName = 'cal_abstract'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/nmuncy/Projects/cal_abstract/cal_abstract.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
welcome_text1 = visual.TextStim(win=win, name='welcome_text1',
    text='Welcome to the Experiment!',
    font='Arial',
    pos=(0, 0.3), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
welcome_text2 = visual.TextStim(win=win, name='welcome_text2',
    text='We appreciate your participation.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
welcome_text3 = visual.TextStim(win=win, name='welcome_text3',
    text='Press “enter” or “return” to continue.',
    font='Arial',
    pos=(0, -0.35), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
welcome_resp = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
instruct_text1 = visual.TextStim(win=win, name='instruct_text1',
    text='default text',
    font='Arial',
    pos=(0, 0.15), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instruct_text2 = visual.TextStim(win=win, name='instruct_text2',
    text='Press “enter” or “return” to continue.',
    font='Arial',
    pos=(0, -0.35), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instruct_resp1 = keyboard.Keyboard()

# Initialize components for Routine "Start1"
Start1Clock = core.Clock()
start_text1 = visual.TextStim(win=win, name='start_text1',
    text='Starting Block 1.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
start_text2 = visual.TextStim(win=win, name='start_text2',
    text='Press “s” to start the block.',
    font='Arial',
    pos=(0, -0.35), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
start_resp1 = keyboard.Keyboard()

# Initialize components for Routine "Block1"
Block1Clock = core.Clock()
image1 = visual.ImageStim(
    win=win,
    name='image1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
respL1 = visual.TextStim(win=win, name='respL1',
    text='default text',
    font='Arial',
    pos=(-0.25, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
textL1 = visual.TextStim(win=win, name='textL1',
    text='left',
    font='Arial',
    pos=(-0.25, -0.45), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
respM1 = visual.TextStim(win=win, name='respM1',
    text='default text',
    font='Arial',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
textM1 = visual.TextStim(win=win, name='textM1',
    text='down',
    font='Arial',
    pos=(0, -0.45), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
respR1 = visual.TextStim(win=win, name='respR1',
    text='default text',
    font='Arial',
    pos=(0.25, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
textR1 = visual.TextStim(win=win, name='textR1',
    text='right',
    font='Arial',
    pos=(0.25, -0.45), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
key_resp1 = keyboard.Keyboard()

# Initialize components for Routine "Feedback1"
Feedback1Clock = core.Clock()
feedback_text1 = visual.TextStim(win=win, name='feedback_text1',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Break1"
Break1Clock = core.Clock()
break_text1 = visual.TextStim(win=win, name='break_text1',
    text='You have finished block 1/3. Feel free to take a short break.\n\nWhen you are ready to continue, press “c”.',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
break_resp1 = keyboard.Keyboard()

# Initialize components for Routine "InstructReminder"
InstructReminderClock = core.Clock()
intructRemind_text1 = visual.TextStim(win=win, name='intructRemind_text1',
    text='Reminder:\n\nSome stimuli always have a correct “Left” response, and others always have a correct “Right” response.\n\nFor others, the correct response is opposite from the previous stimulus.',
    font='Arial',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructRemind_text2 = visual.TextStim(win=win, name='instructRemind_text2',
    text='Press “enter” or “return” to continue.',
    font='Arial',
    pos=(0, -0.35), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instructRemind_resp1 = keyboard.Keyboard()

# Initialize components for Routine "Start2"
Start2Clock = core.Clock()
start_text3 = visual.TextStim(win=win, name='start_text3',
    text='Starting Block 2.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
start_text4 = visual.TextStim(win=win, name='start_text4',
    text='Press “s” to start the block.',
    font='Arial',
    pos=(0, -0.35), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
start_resp2 = keyboard.Keyboard()

# Initialize components for Routine "Block2"
Block2Clock = core.Clock()
image2 = visual.ImageStim(
    win=win,
    name='image2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
respL2 = visual.TextStim(win=win, name='respL2',
    text='default text',
    font='Arial',
    pos=(-0.25, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
textL2 = visual.TextStim(win=win, name='textL2',
    text='left',
    font='Arial',
    pos=(-0.25, -0.45), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
respM2 = visual.TextStim(win=win, name='respM2',
    text='default text',
    font='Arial',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
textM2 = visual.TextStim(win=win, name='textM2',
    text='down',
    font='Arial',
    pos=(0, -0.45), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
respR2 = visual.TextStim(win=win, name='respR2',
    text='default text',
    font='Arial',
    pos=(0.25, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
textR2 = visual.TextStim(win=win, name='textR2',
    text='right',
    font='Arial',
    pos=(0.25, -0.45), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
key_resp2 = keyboard.Keyboard()

# Initialize components for Routine "Feedback2"
Feedback2Clock = core.Clock()
feedback_text2 = visual.TextStim(win=win, name='feedback_text2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Break2"
Break2Clock = core.Clock()
break_text2 = visual.TextStim(win=win, name='break_text2',
    text='You have finished block 2/3. Feel free to take a short break.\n\nWhen you are ready to continue, press “c”.',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
break_resp2 = keyboard.Keyboard()

# Initialize components for Routine "InstructReminder"
InstructReminderClock = core.Clock()
intructRemind_text1 = visual.TextStim(win=win, name='intructRemind_text1',
    text='Reminder:\n\nSome stimuli always have a correct “Left” response, and others always have a correct “Right” response.\n\nFor others, the correct response is opposite from the previous stimulus.',
    font='Arial',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructRemind_text2 = visual.TextStim(win=win, name='instructRemind_text2',
    text='Press “enter” or “return” to continue.',
    font='Arial',
    pos=(0, -0.35), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instructRemind_resp1 = keyboard.Keyboard()

# Initialize components for Routine "Start3"
Start3Clock = core.Clock()
start_text5 = visual.TextStim(win=win, name='start_text5',
    text='Starting Block 3.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
start_text6 = visual.TextStim(win=win, name='start_text6',
    text='Press “s” to start the block.',
    font='Arial',
    pos=(0, -0.35), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
start_resp3 = keyboard.Keyboard()

# Initialize components for Routine "Block3"
Block3Clock = core.Clock()
image3 = visual.ImageStim(
    win=win,
    name='image3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
respL3 = visual.TextStim(win=win, name='respL3',
    text='default text',
    font='Arial',
    pos=(-0.25, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
textL3 = visual.TextStim(win=win, name='textL3',
    text='left',
    font='Arial',
    pos=(-0.25, -0.45), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
respM3 = visual.TextStim(win=win, name='respM3',
    text='default text',
    font='Arial',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
textM3 = visual.TextStim(win=win, name='textM3',
    text='down',
    font='Arial',
    pos=(0, -0.45), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
respR3 = visual.TextStim(win=win, name='respR3',
    text='default text',
    font='Arial',
    pos=(0.25, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
textR3 = visual.TextStim(win=win, name='textR3',
    text='right',
    font='Arial',
    pos=(0.25, -0.45), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
key_resp3 = keyboard.Keyboard()

# Initialize components for Routine "Feedback3"
Feedback3Clock = core.Clock()
feedback_text3 = visual.TextStim(win=win, name='feedback_text3',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "End"
EndClock = core.Clock()
end_text1 = visual.TextStim(win=win, name='end_text1',
    text='You have finished the experiment!',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
end_text2 = visual.TextStim(win=win, name='end_text2',
    text='Press “e” to exit.',
    font='Arial',
    pos=(0, -0.35), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
end_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome"-------
continueRoutine = True
# update component parameters for each repeat
welcome_resp.keys = []
welcome_resp.rt = []
_welcome_resp_allKeys = []
# keep track of which components have finished
WelcomeComponents = [welcome_text1, welcome_text2, welcome_text3, welcome_resp]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Welcome"-------
while continueRoutine:
    # get current time
    t = WelcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_text1* updates
    if welcome_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_text1.frameNStart = frameN  # exact frame index
        welcome_text1.tStart = t  # local t and not account for scr refresh
        welcome_text1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_text1, 'tStartRefresh')  # time at next scr refresh
        welcome_text1.setAutoDraw(True)
    
    # *welcome_text2* updates
    if welcome_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_text2.frameNStart = frameN  # exact frame index
        welcome_text2.tStart = t  # local t and not account for scr refresh
        welcome_text2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_text2, 'tStartRefresh')  # time at next scr refresh
        welcome_text2.setAutoDraw(True)
    
    # *welcome_text3* updates
    if welcome_text3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_text3.frameNStart = frameN  # exact frame index
        welcome_text3.tStart = t  # local t and not account for scr refresh
        welcome_text3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_text3, 'tStartRefresh')  # time at next scr refresh
        welcome_text3.setAutoDraw(True)
    
    # *welcome_resp* updates
    waitOnFlip = False
    if welcome_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_resp.frameNStart = frameN  # exact frame index
        welcome_resp.tStart = t  # local t and not account for scr refresh
        welcome_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_resp, 'tStartRefresh')  # time at next scr refresh
        welcome_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(welcome_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(welcome_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if welcome_resp.status == STARTED and not waitOnFlip:
        theseKeys = welcome_resp.getKeys(keyList=['return'], waitRelease=False)
        _welcome_resp_allKeys.extend(theseKeys)
        if len(_welcome_resp_allKeys):
            welcome_resp.keys = _welcome_resp_allKeys[-1].name  # just the last key pressed
            welcome_resp.rt = _welcome_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome"-------
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('welcome_text1.started', welcome_text1.tStartRefresh)
thisExp.addData('welcome_text1.stopped', welcome_text1.tStopRefresh)
thisExp.addData('welcome_text2.started', welcome_text2.tStartRefresh)
thisExp.addData('welcome_text2.stopped', welcome_text2.tStopRefresh)
thisExp.addData('welcome_text3.started', welcome_text3.tStartRefresh)
thisExp.addData('welcome_text3.stopped', welcome_text3.tStopRefresh)
# check responses
if welcome_resp.keys in ['', [], None]:  # No response was made
    welcome_resp.keys = None
thisExp.addData('welcome_resp.keys',welcome_resp.keys)
if welcome_resp.keys != None:  # we had a response
    thisExp.addData('welcome_resp.rt', welcome_resp.rt)
thisExp.addData('welcome_resp.started', welcome_resp.tStartRefresh)
thisExp.addData('welcome_resp.stopped', welcome_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Instruction_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('instructions/Instructions.xlsx'),
    seed=None, name='Instruction_loop')
thisExp.addLoop(Instruction_loop)  # add the loop to the experiment
thisInstruction_loop = Instruction_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstruction_loop.rgb)
if thisInstruction_loop != None:
    for paramName in thisInstruction_loop:
        exec('{} = thisInstruction_loop[paramName]'.format(paramName))

for thisInstruction_loop in Instruction_loop:
    currentLoop = Instruction_loop
    # abbreviate parameter names if possible (e.g. rgb = thisInstruction_loop.rgb)
    if thisInstruction_loop != None:
        for paramName in thisInstruction_loop:
            exec('{} = thisInstruction_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    instruct_text1.setText(Text)
    instruct_resp1.keys = []
    instruct_resp1.rt = []
    _instruct_resp1_allKeys = []
    # keep track of which components have finished
    InstructionsComponents = [instruct_text1, instruct_text2, instruct_resp1]
    for thisComponent in InstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Instructions"-------
    while continueRoutine:
        # get current time
        t = InstructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruct_text1* updates
        if instruct_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruct_text1.frameNStart = frameN  # exact frame index
            instruct_text1.tStart = t  # local t and not account for scr refresh
            instruct_text1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruct_text1, 'tStartRefresh')  # time at next scr refresh
            instruct_text1.setAutoDraw(True)
        
        # *instruct_text2* updates
        if instruct_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruct_text2.frameNStart = frameN  # exact frame index
            instruct_text2.tStart = t  # local t and not account for scr refresh
            instruct_text2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruct_text2, 'tStartRefresh')  # time at next scr refresh
            instruct_text2.setAutoDraw(True)
        
        # *instruct_resp1* updates
        waitOnFlip = False
        if instruct_resp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruct_resp1.frameNStart = frameN  # exact frame index
            instruct_resp1.tStart = t  # local t and not account for scr refresh
            instruct_resp1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruct_resp1, 'tStartRefresh')  # time at next scr refresh
            instruct_resp1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instruct_resp1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instruct_resp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instruct_resp1.status == STARTED and not waitOnFlip:
            theseKeys = instruct_resp1.getKeys(keyList=['return'], waitRelease=False)
            _instruct_resp1_allKeys.extend(theseKeys)
            if len(_instruct_resp1_allKeys):
                instruct_resp1.keys = _instruct_resp1_allKeys[-1].name  # just the last key pressed
                instruct_resp1.rt = _instruct_resp1_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Instructions"-------
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Instruction_loop.addData('instruct_text1.started', instruct_text1.tStartRefresh)
    Instruction_loop.addData('instruct_text1.stopped', instruct_text1.tStopRefresh)
    Instruction_loop.addData('instruct_text2.started', instruct_text2.tStartRefresh)
    Instruction_loop.addData('instruct_text2.stopped', instruct_text2.tStopRefresh)
    # check responses
    if instruct_resp1.keys in ['', [], None]:  # No response was made
        instruct_resp1.keys = None
    Instruction_loop.addData('instruct_resp1.keys',instruct_resp1.keys)
    if instruct_resp1.keys != None:  # we had a response
        Instruction_loop.addData('instruct_resp1.rt', instruct_resp1.rt)
    Instruction_loop.addData('instruct_resp1.started', instruct_resp1.tStartRefresh)
    Instruction_loop.addData('instruct_resp1.stopped', instruct_resp1.tStopRefresh)
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'Instruction_loop'


# ------Prepare to start Routine "Start1"-------
continueRoutine = True
# update component parameters for each repeat
start_resp1.keys = []
start_resp1.rt = []
_start_resp1_allKeys = []
# keep track of which components have finished
Start1Components = [start_text1, start_text2, start_resp1]
for thisComponent in Start1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Start1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Start1"-------
while continueRoutine:
    # get current time
    t = Start1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Start1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start_text1* updates
    if start_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_text1.frameNStart = frameN  # exact frame index
        start_text1.tStart = t  # local t and not account for scr refresh
        start_text1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_text1, 'tStartRefresh')  # time at next scr refresh
        start_text1.setAutoDraw(True)
    
    # *start_text2* updates
    if start_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_text2.frameNStart = frameN  # exact frame index
        start_text2.tStart = t  # local t and not account for scr refresh
        start_text2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_text2, 'tStartRefresh')  # time at next scr refresh
        start_text2.setAutoDraw(True)
    
    # *start_resp1* updates
    waitOnFlip = False
    if start_resp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_resp1.frameNStart = frameN  # exact frame index
        start_resp1.tStart = t  # local t and not account for scr refresh
        start_resp1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_resp1, 'tStartRefresh')  # time at next scr refresh
        start_resp1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(start_resp1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(start_resp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if start_resp1.status == STARTED and not waitOnFlip:
        theseKeys = start_resp1.getKeys(keyList=['s'], waitRelease=False)
        _start_resp1_allKeys.extend(theseKeys)
        if len(_start_resp1_allKeys):
            start_resp1.keys = _start_resp1_allKeys[-1].name  # just the last key pressed
            start_resp1.rt = _start_resp1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start1"-------
for thisComponent in Start1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('start_text1.started', start_text1.tStartRefresh)
thisExp.addData('start_text1.stopped', start_text1.tStopRefresh)
thisExp.addData('start_text2.started', start_text2.tStartRefresh)
thisExp.addData('start_text2.stopped', start_text2.tStopRefresh)
# check responses
if start_resp1.keys in ['', [], None]:  # No response was made
    start_resp1.keys = None
thisExp.addData('start_resp1.keys',start_resp1.keys)
if start_resp1.keys != None:  # we had a response
    thisExp.addData('start_resp1.rt', start_resp1.rt)
thisExp.addData('start_resp1.started', start_resp1.tStartRefresh)
thisExp.addData('start_resp1.stopped', start_resp1.tStopRefresh)
thisExp.nextEntry()
# the Routine "Start1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Block1_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('blocks/Block1.csv'),
    seed=None, name='Block1_loop')
thisExp.addLoop(Block1_loop)  # add the loop to the experiment
thisBlock1_loop = Block1_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock1_loop.rgb)
if thisBlock1_loop != None:
    for paramName in thisBlock1_loop:
        exec('{} = thisBlock1_loop[paramName]'.format(paramName))

for thisBlock1_loop in Block1_loop:
    currentLoop = Block1_loop
    # abbreviate parameter names if possible (e.g. rgb = thisBlock1_loop.rgb)
    if thisBlock1_loop != None:
        for paramName in thisBlock1_loop:
            exec('{} = thisBlock1_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Block1"-------
    continueRoutine = True
    # update component parameters for each repeat
    image1.setImage(Block1Stim)
    respL1.setText(Block1RespL)
    respM1.setText(Block1RespM)
    respR1.setText(Block1RespR)
    key_resp1.keys = []
    key_resp1.rt = []
    _key_resp1_allKeys = []
    # keep track of which components have finished
    Block1Components = [image1, respL1, textL1, respM1, textM1, respR1, textR1, key_resp1]
    for thisComponent in Block1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Block1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Block1"-------
    while continueRoutine:
        # get current time
        t = Block1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Block1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image1* updates
        if image1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image1.frameNStart = frameN  # exact frame index
            image1.tStart = t  # local t and not account for scr refresh
            image1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image1, 'tStartRefresh')  # time at next scr refresh
            image1.setAutoDraw(True)
        
        # *respL1* updates
        if respL1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            respL1.frameNStart = frameN  # exact frame index
            respL1.tStart = t  # local t and not account for scr refresh
            respL1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respL1, 'tStartRefresh')  # time at next scr refresh
            respL1.setAutoDraw(True)
        
        # *textL1* updates
        if textL1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textL1.frameNStart = frameN  # exact frame index
            textL1.tStart = t  # local t and not account for scr refresh
            textL1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textL1, 'tStartRefresh')  # time at next scr refresh
            textL1.setAutoDraw(True)
        
        # *respM1* updates
        if respM1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            respM1.frameNStart = frameN  # exact frame index
            respM1.tStart = t  # local t and not account for scr refresh
            respM1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respM1, 'tStartRefresh')  # time at next scr refresh
            respM1.setAutoDraw(True)
        
        # *textM1* updates
        if textM1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textM1.frameNStart = frameN  # exact frame index
            textM1.tStart = t  # local t and not account for scr refresh
            textM1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textM1, 'tStartRefresh')  # time at next scr refresh
            textM1.setAutoDraw(True)
        
        # *respR1* updates
        if respR1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            respR1.frameNStart = frameN  # exact frame index
            respR1.tStart = t  # local t and not account for scr refresh
            respR1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respR1, 'tStartRefresh')  # time at next scr refresh
            respR1.setAutoDraw(True)
        
        # *textR1* updates
        if textR1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textR1.frameNStart = frameN  # exact frame index
            textR1.tStart = t  # local t and not account for scr refresh
            textR1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textR1, 'tStartRefresh')  # time at next scr refresh
            textR1.setAutoDraw(True)
        
        # *key_resp1* updates
        waitOnFlip = False
        if key_resp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp1.frameNStart = frameN  # exact frame index
            key_resp1.tStart = t  # local t and not account for scr refresh
            key_resp1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp1, 'tStartRefresh')  # time at next scr refresh
            key_resp1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp1.status == STARTED and not waitOnFlip:
            theseKeys = key_resp1.getKeys(keyList=['left', 'right', 'down'], waitRelease=False)
            _key_resp1_allKeys.extend(theseKeys)
            if len(_key_resp1_allKeys):
                key_resp1.keys = _key_resp1_allKeys[-1].name  # just the last key pressed
                key_resp1.rt = _key_resp1_allKeys[-1].rt
                # was this correct?
                if (key_resp1.keys == str(Block1Corr)) or (key_resp1.keys == Block1Corr):
                    key_resp1.corr = 1
                else:
                    key_resp1.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Block1"-------
    for thisComponent in Block1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Block1_loop.addData('image1.started', image1.tStartRefresh)
    Block1_loop.addData('image1.stopped', image1.tStopRefresh)
    Block1_loop.addData('respL1.started', respL1.tStartRefresh)
    Block1_loop.addData('respL1.stopped', respL1.tStopRefresh)
    Block1_loop.addData('textL1.started', textL1.tStartRefresh)
    Block1_loop.addData('textL1.stopped', textL1.tStopRefresh)
    Block1_loop.addData('respM1.started', respM1.tStartRefresh)
    Block1_loop.addData('respM1.stopped', respM1.tStopRefresh)
    Block1_loop.addData('textM1.started', textM1.tStartRefresh)
    Block1_loop.addData('textM1.stopped', textM1.tStopRefresh)
    Block1_loop.addData('respR1.started', respR1.tStartRefresh)
    Block1_loop.addData('respR1.stopped', respR1.tStopRefresh)
    Block1_loop.addData('textR1.started', textR1.tStartRefresh)
    Block1_loop.addData('textR1.stopped', textR1.tStopRefresh)
    # check responses
    if key_resp1.keys in ['', [], None]:  # No response was made
        key_resp1.keys = None
        # was no response the correct answer?!
        if str(Block1Corr).lower() == 'none':
           key_resp1.corr = 1;  # correct non-response
        else:
           key_resp1.corr = 0;  # failed to respond (incorrectly)
    # store data for Block1_loop (TrialHandler)
    Block1_loop.addData('key_resp1.keys',key_resp1.keys)
    Block1_loop.addData('key_resp1.corr', key_resp1.corr)
    if key_resp1.keys != None:  # we had a response
        Block1_loop.addData('key_resp1.rt', key_resp1.rt)
    Block1_loop.addData('key_resp1.started', key_resp1.tStartRefresh)
    Block1_loop.addData('key_resp1.stopped', key_resp1.tStopRefresh)
    # the Routine "Block1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Feedback1"-------
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    if key_resp1.keys == Block1CorrAlpha:
        trialFeedback1 = 'Correct!'
        trialBinary1 = 1
    else:
        trialFeedback1 = 'Incorrect'
        trialBinary1 = 0
    
    Block1_loop.addData('trialCorrect', trialBinary1)
    feedback_text1.setText(trialFeedback1)
    # keep track of which components have finished
    Feedback1Components = [feedback_text1]
    for thisComponent in Feedback1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Feedback1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Feedback1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Feedback1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Feedback1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_text1* updates
        if feedback_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_text1.frameNStart = frameN  # exact frame index
            feedback_text1.tStart = t  # local t and not account for scr refresh
            feedback_text1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_text1, 'tStartRefresh')  # time at next scr refresh
            feedback_text1.setAutoDraw(True)
        if feedback_text1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_text1.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                feedback_text1.tStop = t  # not accounting for scr refresh
                feedback_text1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback_text1, 'tStopRefresh')  # time at next scr refresh
                feedback_text1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Feedback1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback1"-------
    for thisComponent in Feedback1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Block1_loop.addData('feedback_text1.started', feedback_text1.tStartRefresh)
    Block1_loop.addData('feedback_text1.stopped', feedback_text1.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'Block1_loop'


# ------Prepare to start Routine "Break1"-------
continueRoutine = True
# update component parameters for each repeat
break_resp1.keys = []
break_resp1.rt = []
_break_resp1_allKeys = []
# keep track of which components have finished
Break1Components = [break_text1, break_resp1]
for thisComponent in Break1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Break1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Break1"-------
while continueRoutine:
    # get current time
    t = Break1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Break1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *break_text1* updates
    if break_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        break_text1.frameNStart = frameN  # exact frame index
        break_text1.tStart = t  # local t and not account for scr refresh
        break_text1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(break_text1, 'tStartRefresh')  # time at next scr refresh
        break_text1.setAutoDraw(True)
    
    # *break_resp1* updates
    waitOnFlip = False
    if break_resp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        break_resp1.frameNStart = frameN  # exact frame index
        break_resp1.tStart = t  # local t and not account for scr refresh
        break_resp1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(break_resp1, 'tStartRefresh')  # time at next scr refresh
        break_resp1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(break_resp1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(break_resp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if break_resp1.status == STARTED and not waitOnFlip:
        theseKeys = break_resp1.getKeys(keyList=['c'], waitRelease=False)
        _break_resp1_allKeys.extend(theseKeys)
        if len(_break_resp1_allKeys):
            break_resp1.keys = _break_resp1_allKeys[-1].name  # just the last key pressed
            break_resp1.rt = _break_resp1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Break1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Break1"-------
for thisComponent in Break1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('break_text1.started', break_text1.tStartRefresh)
thisExp.addData('break_text1.stopped', break_text1.tStopRefresh)
# check responses
if break_resp1.keys in ['', [], None]:  # No response was made
    break_resp1.keys = None
thisExp.addData('break_resp1.keys',break_resp1.keys)
if break_resp1.keys != None:  # we had a response
    thisExp.addData('break_resp1.rt', break_resp1.rt)
thisExp.addData('break_resp1.started', break_resp1.tStartRefresh)
thisExp.addData('break_resp1.stopped', break_resp1.tStopRefresh)
thisExp.nextEntry()
# the Routine "Break1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "InstructReminder"-------
continueRoutine = True
# update component parameters for each repeat
instructRemind_resp1.keys = []
instructRemind_resp1.rt = []
_instructRemind_resp1_allKeys = []
# keep track of which components have finished
InstructReminderComponents = [intructRemind_text1, instructRemind_text2, instructRemind_resp1]
for thisComponent in InstructReminderComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructReminderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "InstructReminder"-------
while continueRoutine:
    # get current time
    t = InstructReminderClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructReminderClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intructRemind_text1* updates
    if intructRemind_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intructRemind_text1.frameNStart = frameN  # exact frame index
        intructRemind_text1.tStart = t  # local t and not account for scr refresh
        intructRemind_text1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intructRemind_text1, 'tStartRefresh')  # time at next scr refresh
        intructRemind_text1.setAutoDraw(True)
    
    # *instructRemind_text2* updates
    if instructRemind_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructRemind_text2.frameNStart = frameN  # exact frame index
        instructRemind_text2.tStart = t  # local t and not account for scr refresh
        instructRemind_text2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRemind_text2, 'tStartRefresh')  # time at next scr refresh
        instructRemind_text2.setAutoDraw(True)
    
    # *instructRemind_resp1* updates
    waitOnFlip = False
    if instructRemind_resp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructRemind_resp1.frameNStart = frameN  # exact frame index
        instructRemind_resp1.tStart = t  # local t and not account for scr refresh
        instructRemind_resp1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRemind_resp1, 'tStartRefresh')  # time at next scr refresh
        instructRemind_resp1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructRemind_resp1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructRemind_resp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructRemind_resp1.status == STARTED and not waitOnFlip:
        theseKeys = instructRemind_resp1.getKeys(keyList=['return'], waitRelease=False)
        _instructRemind_resp1_allKeys.extend(theseKeys)
        if len(_instructRemind_resp1_allKeys):
            instructRemind_resp1.keys = _instructRemind_resp1_allKeys[-1].name  # just the last key pressed
            instructRemind_resp1.rt = _instructRemind_resp1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructReminderComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InstructReminder"-------
for thisComponent in InstructReminderComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('intructRemind_text1.started', intructRemind_text1.tStartRefresh)
thisExp.addData('intructRemind_text1.stopped', intructRemind_text1.tStopRefresh)
thisExp.addData('instructRemind_text2.started', instructRemind_text2.tStartRefresh)
thisExp.addData('instructRemind_text2.stopped', instructRemind_text2.tStopRefresh)
# check responses
if instructRemind_resp1.keys in ['', [], None]:  # No response was made
    instructRemind_resp1.keys = None
thisExp.addData('instructRemind_resp1.keys',instructRemind_resp1.keys)
if instructRemind_resp1.keys != None:  # we had a response
    thisExp.addData('instructRemind_resp1.rt', instructRemind_resp1.rt)
thisExp.addData('instructRemind_resp1.started', instructRemind_resp1.tStartRefresh)
thisExp.addData('instructRemind_resp1.stopped', instructRemind_resp1.tStopRefresh)
thisExp.nextEntry()
# the Routine "InstructReminder" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Start2"-------
continueRoutine = True
# update component parameters for each repeat
start_resp2.keys = []
start_resp2.rt = []
_start_resp2_allKeys = []
# keep track of which components have finished
Start2Components = [start_text3, start_text4, start_resp2]
for thisComponent in Start2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Start2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Start2"-------
while continueRoutine:
    # get current time
    t = Start2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Start2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start_text3* updates
    if start_text3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_text3.frameNStart = frameN  # exact frame index
        start_text3.tStart = t  # local t and not account for scr refresh
        start_text3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_text3, 'tStartRefresh')  # time at next scr refresh
        start_text3.setAutoDraw(True)
    
    # *start_text4* updates
    if start_text4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_text4.frameNStart = frameN  # exact frame index
        start_text4.tStart = t  # local t and not account for scr refresh
        start_text4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_text4, 'tStartRefresh')  # time at next scr refresh
        start_text4.setAutoDraw(True)
    
    # *start_resp2* updates
    waitOnFlip = False
    if start_resp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_resp2.frameNStart = frameN  # exact frame index
        start_resp2.tStart = t  # local t and not account for scr refresh
        start_resp2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_resp2, 'tStartRefresh')  # time at next scr refresh
        start_resp2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(start_resp2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(start_resp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if start_resp2.status == STARTED and not waitOnFlip:
        theseKeys = start_resp2.getKeys(keyList=['s'], waitRelease=False)
        _start_resp2_allKeys.extend(theseKeys)
        if len(_start_resp2_allKeys):
            start_resp2.keys = _start_resp2_allKeys[-1].name  # just the last key pressed
            start_resp2.rt = _start_resp2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start2"-------
for thisComponent in Start2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('start_text3.started', start_text3.tStartRefresh)
thisExp.addData('start_text3.stopped', start_text3.tStopRefresh)
thisExp.addData('start_text4.started', start_text4.tStartRefresh)
thisExp.addData('start_text4.stopped', start_text4.tStopRefresh)
# check responses
if start_resp2.keys in ['', [], None]:  # No response was made
    start_resp2.keys = None
thisExp.addData('start_resp2.keys',start_resp2.keys)
if start_resp2.keys != None:  # we had a response
    thisExp.addData('start_resp2.rt', start_resp2.rt)
thisExp.addData('start_resp2.started', start_resp2.tStartRefresh)
thisExp.addData('start_resp2.stopped', start_resp2.tStopRefresh)
thisExp.nextEntry()
# the Routine "Start2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Block2_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('blocks/Block2.csv'),
    seed=None, name='Block2_loop')
thisExp.addLoop(Block2_loop)  # add the loop to the experiment
thisBlock2_loop = Block2_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock2_loop.rgb)
if thisBlock2_loop != None:
    for paramName in thisBlock2_loop:
        exec('{} = thisBlock2_loop[paramName]'.format(paramName))

for thisBlock2_loop in Block2_loop:
    currentLoop = Block2_loop
    # abbreviate parameter names if possible (e.g. rgb = thisBlock2_loop.rgb)
    if thisBlock2_loop != None:
        for paramName in thisBlock2_loop:
            exec('{} = thisBlock2_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Block2"-------
    continueRoutine = True
    # update component parameters for each repeat
    image2.setImage(Block2Stim)
    respL2.setText(Block2RespL)
    respM2.setText(Block2RespM)
    respR2.setText(Block2RespR)
    key_resp2.keys = []
    key_resp2.rt = []
    _key_resp2_allKeys = []
    # keep track of which components have finished
    Block2Components = [image2, respL2, textL2, respM2, textM2, respR2, textR2, key_resp2]
    for thisComponent in Block2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Block2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Block2"-------
    while continueRoutine:
        # get current time
        t = Block2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Block2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image2* updates
        if image2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image2.frameNStart = frameN  # exact frame index
            image2.tStart = t  # local t and not account for scr refresh
            image2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image2, 'tStartRefresh')  # time at next scr refresh
            image2.setAutoDraw(True)
        
        # *respL2* updates
        if respL2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            respL2.frameNStart = frameN  # exact frame index
            respL2.tStart = t  # local t and not account for scr refresh
            respL2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respL2, 'tStartRefresh')  # time at next scr refresh
            respL2.setAutoDraw(True)
        
        # *textL2* updates
        if textL2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textL2.frameNStart = frameN  # exact frame index
            textL2.tStart = t  # local t and not account for scr refresh
            textL2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textL2, 'tStartRefresh')  # time at next scr refresh
            textL2.setAutoDraw(True)
        
        # *respM2* updates
        if respM2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            respM2.frameNStart = frameN  # exact frame index
            respM2.tStart = t  # local t and not account for scr refresh
            respM2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respM2, 'tStartRefresh')  # time at next scr refresh
            respM2.setAutoDraw(True)
        
        # *textM2* updates
        if textM2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textM2.frameNStart = frameN  # exact frame index
            textM2.tStart = t  # local t and not account for scr refresh
            textM2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textM2, 'tStartRefresh')  # time at next scr refresh
            textM2.setAutoDraw(True)
        
        # *respR2* updates
        if respR2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            respR2.frameNStart = frameN  # exact frame index
            respR2.tStart = t  # local t and not account for scr refresh
            respR2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respR2, 'tStartRefresh')  # time at next scr refresh
            respR2.setAutoDraw(True)
        
        # *textR2* updates
        if textR2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textR2.frameNStart = frameN  # exact frame index
            textR2.tStart = t  # local t and not account for scr refresh
            textR2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textR2, 'tStartRefresh')  # time at next scr refresh
            textR2.setAutoDraw(True)
        
        # *key_resp2* updates
        waitOnFlip = False
        if key_resp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp2.frameNStart = frameN  # exact frame index
            key_resp2.tStart = t  # local t and not account for scr refresh
            key_resp2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp2, 'tStartRefresh')  # time at next scr refresh
            key_resp2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp2.getKeys(keyList=['left', 'right', 'down'], waitRelease=False)
            _key_resp2_allKeys.extend(theseKeys)
            if len(_key_resp2_allKeys):
                key_resp2.keys = _key_resp2_allKeys[-1].name  # just the last key pressed
                key_resp2.rt = _key_resp2_allKeys[-1].rt
                # was this correct?
                if (key_resp2.keys == str(Block2Corr)) or (key_resp2.keys == Block2Corr):
                    key_resp2.corr = 1
                else:
                    key_resp2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Block2"-------
    for thisComponent in Block2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Block2_loop.addData('image2.started', image2.tStartRefresh)
    Block2_loop.addData('image2.stopped', image2.tStopRefresh)
    Block2_loop.addData('respL2.started', respL2.tStartRefresh)
    Block2_loop.addData('respL2.stopped', respL2.tStopRefresh)
    Block2_loop.addData('textL2.started', textL2.tStartRefresh)
    Block2_loop.addData('textL2.stopped', textL2.tStopRefresh)
    Block2_loop.addData('respM2.started', respM2.tStartRefresh)
    Block2_loop.addData('respM2.stopped', respM2.tStopRefresh)
    Block2_loop.addData('textM2.started', textM2.tStartRefresh)
    Block2_loop.addData('textM2.stopped', textM2.tStopRefresh)
    Block2_loop.addData('respR2.started', respR2.tStartRefresh)
    Block2_loop.addData('respR2.stopped', respR2.tStopRefresh)
    Block2_loop.addData('textR2.started', textR2.tStartRefresh)
    Block2_loop.addData('textR2.stopped', textR2.tStopRefresh)
    # check responses
    if key_resp2.keys in ['', [], None]:  # No response was made
        key_resp2.keys = None
        # was no response the correct answer?!
        if str(Block2Corr).lower() == 'none':
           key_resp2.corr = 1;  # correct non-response
        else:
           key_resp2.corr = 0;  # failed to respond (incorrectly)
    # store data for Block2_loop (TrialHandler)
    Block2_loop.addData('key_resp2.keys',key_resp2.keys)
    Block2_loop.addData('key_resp2.corr', key_resp2.corr)
    if key_resp2.keys != None:  # we had a response
        Block2_loop.addData('key_resp2.rt', key_resp2.rt)
    Block2_loop.addData('key_resp2.started', key_resp2.tStartRefresh)
    Block2_loop.addData('key_resp2.stopped', key_resp2.tStopRefresh)
    # the Routine "Block2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Feedback2"-------
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    if key_resp2.keys == Block2CorrAlpha:
        trialFeedback2 = 'Correct!'
        trialBinary2 = 1
    else:
        trialFeedback2 = 'Incorrect'
        trialBinary2 = 0
    
    Block2_loop.addData('trialCorrect', trialBinary2)
    feedback_text2.setText(trialFeedback2)
    # keep track of which components have finished
    Feedback2Components = [feedback_text2]
    for thisComponent in Feedback2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Feedback2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Feedback2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Feedback2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Feedback2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_text2* updates
        if feedback_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_text2.frameNStart = frameN  # exact frame index
            feedback_text2.tStart = t  # local t and not account for scr refresh
            feedback_text2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_text2, 'tStartRefresh')  # time at next scr refresh
            feedback_text2.setAutoDraw(True)
        if feedback_text2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_text2.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                feedback_text2.tStop = t  # not accounting for scr refresh
                feedback_text2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback_text2, 'tStopRefresh')  # time at next scr refresh
                feedback_text2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Feedback2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback2"-------
    for thisComponent in Feedback2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Block2_loop.addData('feedback_text2.started', feedback_text2.tStartRefresh)
    Block2_loop.addData('feedback_text2.stopped', feedback_text2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'Block2_loop'


# ------Prepare to start Routine "Break2"-------
continueRoutine = True
# update component parameters for each repeat
break_resp2.keys = []
break_resp2.rt = []
_break_resp2_allKeys = []
# keep track of which components have finished
Break2Components = [break_text2, break_resp2]
for thisComponent in Break2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Break2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Break2"-------
while continueRoutine:
    # get current time
    t = Break2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Break2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *break_text2* updates
    if break_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        break_text2.frameNStart = frameN  # exact frame index
        break_text2.tStart = t  # local t and not account for scr refresh
        break_text2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(break_text2, 'tStartRefresh')  # time at next scr refresh
        break_text2.setAutoDraw(True)
    
    # *break_resp2* updates
    waitOnFlip = False
    if break_resp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        break_resp2.frameNStart = frameN  # exact frame index
        break_resp2.tStart = t  # local t and not account for scr refresh
        break_resp2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(break_resp2, 'tStartRefresh')  # time at next scr refresh
        break_resp2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(break_resp2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(break_resp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if break_resp2.status == STARTED and not waitOnFlip:
        theseKeys = break_resp2.getKeys(keyList=['c'], waitRelease=False)
        _break_resp2_allKeys.extend(theseKeys)
        if len(_break_resp2_allKeys):
            break_resp2.keys = _break_resp2_allKeys[-1].name  # just the last key pressed
            break_resp2.rt = _break_resp2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Break2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Break2"-------
for thisComponent in Break2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('break_text2.started', break_text2.tStartRefresh)
thisExp.addData('break_text2.stopped', break_text2.tStopRefresh)
# check responses
if break_resp2.keys in ['', [], None]:  # No response was made
    break_resp2.keys = None
thisExp.addData('break_resp2.keys',break_resp2.keys)
if break_resp2.keys != None:  # we had a response
    thisExp.addData('break_resp2.rt', break_resp2.rt)
thisExp.addData('break_resp2.started', break_resp2.tStartRefresh)
thisExp.addData('break_resp2.stopped', break_resp2.tStopRefresh)
thisExp.nextEntry()
# the Routine "Break2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "InstructReminder"-------
continueRoutine = True
# update component parameters for each repeat
instructRemind_resp1.keys = []
instructRemind_resp1.rt = []
_instructRemind_resp1_allKeys = []
# keep track of which components have finished
InstructReminderComponents = [intructRemind_text1, instructRemind_text2, instructRemind_resp1]
for thisComponent in InstructReminderComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructReminderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "InstructReminder"-------
while continueRoutine:
    # get current time
    t = InstructReminderClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructReminderClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intructRemind_text1* updates
    if intructRemind_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intructRemind_text1.frameNStart = frameN  # exact frame index
        intructRemind_text1.tStart = t  # local t and not account for scr refresh
        intructRemind_text1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intructRemind_text1, 'tStartRefresh')  # time at next scr refresh
        intructRemind_text1.setAutoDraw(True)
    
    # *instructRemind_text2* updates
    if instructRemind_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructRemind_text2.frameNStart = frameN  # exact frame index
        instructRemind_text2.tStart = t  # local t and not account for scr refresh
        instructRemind_text2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRemind_text2, 'tStartRefresh')  # time at next scr refresh
        instructRemind_text2.setAutoDraw(True)
    
    # *instructRemind_resp1* updates
    waitOnFlip = False
    if instructRemind_resp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructRemind_resp1.frameNStart = frameN  # exact frame index
        instructRemind_resp1.tStart = t  # local t and not account for scr refresh
        instructRemind_resp1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructRemind_resp1, 'tStartRefresh')  # time at next scr refresh
        instructRemind_resp1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructRemind_resp1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructRemind_resp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructRemind_resp1.status == STARTED and not waitOnFlip:
        theseKeys = instructRemind_resp1.getKeys(keyList=['return'], waitRelease=False)
        _instructRemind_resp1_allKeys.extend(theseKeys)
        if len(_instructRemind_resp1_allKeys):
            instructRemind_resp1.keys = _instructRemind_resp1_allKeys[-1].name  # just the last key pressed
            instructRemind_resp1.rt = _instructRemind_resp1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructReminderComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InstructReminder"-------
for thisComponent in InstructReminderComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('intructRemind_text1.started', intructRemind_text1.tStartRefresh)
thisExp.addData('intructRemind_text1.stopped', intructRemind_text1.tStopRefresh)
thisExp.addData('instructRemind_text2.started', instructRemind_text2.tStartRefresh)
thisExp.addData('instructRemind_text2.stopped', instructRemind_text2.tStopRefresh)
# check responses
if instructRemind_resp1.keys in ['', [], None]:  # No response was made
    instructRemind_resp1.keys = None
thisExp.addData('instructRemind_resp1.keys',instructRemind_resp1.keys)
if instructRemind_resp1.keys != None:  # we had a response
    thisExp.addData('instructRemind_resp1.rt', instructRemind_resp1.rt)
thisExp.addData('instructRemind_resp1.started', instructRemind_resp1.tStartRefresh)
thisExp.addData('instructRemind_resp1.stopped', instructRemind_resp1.tStopRefresh)
thisExp.nextEntry()
# the Routine "InstructReminder" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Start3"-------
continueRoutine = True
# update component parameters for each repeat
start_resp3.keys = []
start_resp3.rt = []
_start_resp3_allKeys = []
# keep track of which components have finished
Start3Components = [start_text5, start_text6, start_resp3]
for thisComponent in Start3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Start3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Start3"-------
while continueRoutine:
    # get current time
    t = Start3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Start3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start_text5* updates
    if start_text5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_text5.frameNStart = frameN  # exact frame index
        start_text5.tStart = t  # local t and not account for scr refresh
        start_text5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_text5, 'tStartRefresh')  # time at next scr refresh
        start_text5.setAutoDraw(True)
    
    # *start_text6* updates
    if start_text6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_text6.frameNStart = frameN  # exact frame index
        start_text6.tStart = t  # local t and not account for scr refresh
        start_text6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_text6, 'tStartRefresh')  # time at next scr refresh
        start_text6.setAutoDraw(True)
    
    # *start_resp3* updates
    waitOnFlip = False
    if start_resp3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_resp3.frameNStart = frameN  # exact frame index
        start_resp3.tStart = t  # local t and not account for scr refresh
        start_resp3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_resp3, 'tStartRefresh')  # time at next scr refresh
        start_resp3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(start_resp3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(start_resp3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if start_resp3.status == STARTED and not waitOnFlip:
        theseKeys = start_resp3.getKeys(keyList=['s'], waitRelease=False)
        _start_resp3_allKeys.extend(theseKeys)
        if len(_start_resp3_allKeys):
            start_resp3.keys = _start_resp3_allKeys[-1].name  # just the last key pressed
            start_resp3.rt = _start_resp3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start3"-------
for thisComponent in Start3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('start_text5.started', start_text5.tStartRefresh)
thisExp.addData('start_text5.stopped', start_text5.tStopRefresh)
thisExp.addData('start_text6.started', start_text6.tStartRefresh)
thisExp.addData('start_text6.stopped', start_text6.tStopRefresh)
# check responses
if start_resp3.keys in ['', [], None]:  # No response was made
    start_resp3.keys = None
thisExp.addData('start_resp3.keys',start_resp3.keys)
if start_resp3.keys != None:  # we had a response
    thisExp.addData('start_resp3.rt', start_resp3.rt)
thisExp.addData('start_resp3.started', start_resp3.tStartRefresh)
thisExp.addData('start_resp3.stopped', start_resp3.tStopRefresh)
thisExp.nextEntry()
# the Routine "Start3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Block3_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('blocks/Block3.csv'),
    seed=None, name='Block3_loop')
thisExp.addLoop(Block3_loop)  # add the loop to the experiment
thisBlock3_loop = Block3_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock3_loop.rgb)
if thisBlock3_loop != None:
    for paramName in thisBlock3_loop:
        exec('{} = thisBlock3_loop[paramName]'.format(paramName))

for thisBlock3_loop in Block3_loop:
    currentLoop = Block3_loop
    # abbreviate parameter names if possible (e.g. rgb = thisBlock3_loop.rgb)
    if thisBlock3_loop != None:
        for paramName in thisBlock3_loop:
            exec('{} = thisBlock3_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Block3"-------
    continueRoutine = True
    # update component parameters for each repeat
    image3.setImage(Block3Stim)
    respL3.setText(Block3RespL)
    respM3.setText(Block3RespM)
    respR3.setText(Block3RespR)
    key_resp3.keys = []
    key_resp3.rt = []
    _key_resp3_allKeys = []
    # keep track of which components have finished
    Block3Components = [image3, respL3, textL3, respM3, textM3, respR3, textR3, key_resp3]
    for thisComponent in Block3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Block3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Block3"-------
    while continueRoutine:
        # get current time
        t = Block3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Block3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image3* updates
        if image3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image3.frameNStart = frameN  # exact frame index
            image3.tStart = t  # local t and not account for scr refresh
            image3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image3, 'tStartRefresh')  # time at next scr refresh
            image3.setAutoDraw(True)
        
        # *respL3* updates
        if respL3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            respL3.frameNStart = frameN  # exact frame index
            respL3.tStart = t  # local t and not account for scr refresh
            respL3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respL3, 'tStartRefresh')  # time at next scr refresh
            respL3.setAutoDraw(True)
        
        # *textL3* updates
        if textL3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textL3.frameNStart = frameN  # exact frame index
            textL3.tStart = t  # local t and not account for scr refresh
            textL3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textL3, 'tStartRefresh')  # time at next scr refresh
            textL3.setAutoDraw(True)
        
        # *respM3* updates
        if respM3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            respM3.frameNStart = frameN  # exact frame index
            respM3.tStart = t  # local t and not account for scr refresh
            respM3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respM3, 'tStartRefresh')  # time at next scr refresh
            respM3.setAutoDraw(True)
        
        # *textM3* updates
        if textM3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textM3.frameNStart = frameN  # exact frame index
            textM3.tStart = t  # local t and not account for scr refresh
            textM3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textM3, 'tStartRefresh')  # time at next scr refresh
            textM3.setAutoDraw(True)
        
        # *respR3* updates
        if respR3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            respR3.frameNStart = frameN  # exact frame index
            respR3.tStart = t  # local t and not account for scr refresh
            respR3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(respR3, 'tStartRefresh')  # time at next scr refresh
            respR3.setAutoDraw(True)
        
        # *textR3* updates
        if textR3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textR3.frameNStart = frameN  # exact frame index
            textR3.tStart = t  # local t and not account for scr refresh
            textR3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textR3, 'tStartRefresh')  # time at next scr refresh
            textR3.setAutoDraw(True)
        
        # *key_resp3* updates
        waitOnFlip = False
        if key_resp3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp3.frameNStart = frameN  # exact frame index
            key_resp3.tStart = t  # local t and not account for scr refresh
            key_resp3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp3, 'tStartRefresh')  # time at next scr refresh
            key_resp3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp3.getKeys(keyList=['left', 'right', 'down'], waitRelease=False)
            _key_resp3_allKeys.extend(theseKeys)
            if len(_key_resp3_allKeys):
                key_resp3.keys = _key_resp3_allKeys[-1].name  # just the last key pressed
                key_resp3.rt = _key_resp3_allKeys[-1].rt
                # was this correct?
                if (key_resp3.keys == str(Block3Corr)) or (key_resp3.keys == Block3Corr):
                    key_resp3.corr = 1
                else:
                    key_resp3.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Block3"-------
    for thisComponent in Block3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Block3_loop.addData('image3.started', image3.tStartRefresh)
    Block3_loop.addData('image3.stopped', image3.tStopRefresh)
    Block3_loop.addData('respL3.started', respL3.tStartRefresh)
    Block3_loop.addData('respL3.stopped', respL3.tStopRefresh)
    Block3_loop.addData('textL3.started', textL3.tStartRefresh)
    Block3_loop.addData('textL3.stopped', textL3.tStopRefresh)
    Block3_loop.addData('respM3.started', respM3.tStartRefresh)
    Block3_loop.addData('respM3.stopped', respM3.tStopRefresh)
    Block3_loop.addData('textM3.started', textM3.tStartRefresh)
    Block3_loop.addData('textM3.stopped', textM3.tStopRefresh)
    Block3_loop.addData('respR3.started', respR3.tStartRefresh)
    Block3_loop.addData('respR3.stopped', respR3.tStopRefresh)
    Block3_loop.addData('textR3.started', textR3.tStartRefresh)
    Block3_loop.addData('textR3.stopped', textR3.tStopRefresh)
    # check responses
    if key_resp3.keys in ['', [], None]:  # No response was made
        key_resp3.keys = None
        # was no response the correct answer?!
        if str(Block3Corr).lower() == 'none':
           key_resp3.corr = 1;  # correct non-response
        else:
           key_resp3.corr = 0;  # failed to respond (incorrectly)
    # store data for Block3_loop (TrialHandler)
    Block3_loop.addData('key_resp3.keys',key_resp3.keys)
    Block3_loop.addData('key_resp3.corr', key_resp3.corr)
    if key_resp3.keys != None:  # we had a response
        Block3_loop.addData('key_resp3.rt', key_resp3.rt)
    Block3_loop.addData('key_resp3.started', key_resp3.tStartRefresh)
    Block3_loop.addData('key_resp3.stopped', key_resp3.tStopRefresh)
    # the Routine "Block3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Feedback3"-------
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    if key_resp3.keys == Block3CorrAlpha:
        trialFeedback3 = 'Correct!'
        trialBinary3 = 1
    else:
        trialFeedback3 = 'Incorrect'
        trialBinary3 = 0
    
    Block2_loop.addData('trialCorrect', trialBinary3)
    feedback_text3.setText(trialFeedback3)
    # keep track of which components have finished
    Feedback3Components = [feedback_text3]
    for thisComponent in Feedback3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Feedback3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Feedback3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Feedback3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Feedback3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_text3* updates
        if feedback_text3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_text3.frameNStart = frameN  # exact frame index
            feedback_text3.tStart = t  # local t and not account for scr refresh
            feedback_text3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_text3, 'tStartRefresh')  # time at next scr refresh
            feedback_text3.setAutoDraw(True)
        if feedback_text3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_text3.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                feedback_text3.tStop = t  # not accounting for scr refresh
                feedback_text3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback_text3, 'tStopRefresh')  # time at next scr refresh
                feedback_text3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Feedback3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback3"-------
    for thisComponent in Feedback3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Block3_loop.addData('feedback_text3.started', feedback_text3.tStartRefresh)
    Block3_loop.addData('feedback_text3.stopped', feedback_text3.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'Block3_loop'


# ------Prepare to start Routine "End"-------
continueRoutine = True
# update component parameters for each repeat
end_resp.keys = []
end_resp.rt = []
_end_resp_allKeys = []
# keep track of which components have finished
EndComponents = [end_text1, end_text2, end_resp]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End"-------
while continueRoutine:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text1* updates
    if end_text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text1.frameNStart = frameN  # exact frame index
        end_text1.tStart = t  # local t and not account for scr refresh
        end_text1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text1, 'tStartRefresh')  # time at next scr refresh
        end_text1.setAutoDraw(True)
    
    # *end_text2* updates
    if end_text2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text2.frameNStart = frameN  # exact frame index
        end_text2.tStart = t  # local t and not account for scr refresh
        end_text2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text2, 'tStartRefresh')  # time at next scr refresh
        end_text2.setAutoDraw(True)
    
    # *end_resp* updates
    waitOnFlip = False
    if end_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_resp.frameNStart = frameN  # exact frame index
        end_resp.tStart = t  # local t and not account for scr refresh
        end_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_resp, 'tStartRefresh')  # time at next scr refresh
        end_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_resp.status == STARTED and not waitOnFlip:
        theseKeys = end_resp.getKeys(keyList=['e'], waitRelease=False)
        _end_resp_allKeys.extend(theseKeys)
        if len(_end_resp_allKeys):
            end_resp.keys = _end_resp_allKeys[-1].name  # just the last key pressed
            end_resp.rt = _end_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('end_text1.started', end_text1.tStartRefresh)
thisExp.addData('end_text1.stopped', end_text1.tStopRefresh)
thisExp.addData('end_text2.started', end_text2.tStartRefresh)
thisExp.addData('end_text2.stopped', end_text2.tStopRefresh)
# check responses
if end_resp.keys in ['', [], None]:  # No response was made
    end_resp.keys = None
thisExp.addData('end_resp.keys',end_resp.keys)
if end_resp.keys != None:  # we had a response
    thisExp.addData('end_resp.rt', end_resp.rt)
thisExp.addData('end_resp.started', end_resp.tStartRefresh)
thisExp.addData('end_resp.stopped', end_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
