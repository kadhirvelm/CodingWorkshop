import React from 'react'
import ReactDOM from 'react-dom'
import App from './App'

import { createStore, applyMiddleware } from 'redux'
import { Provider } from 'react-redux'
import thunkMiddleware from 'redux-thunk'
import injectTapEventPlugin from 'react-tap-event-plugin'

import proj3 from './State/Reducers'
import { saveState, loadState } from './State/StateStoreLoad'

import * as _colors from 'material-ui/styles/colors'

import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'
import { getMuiTheme } from 'material-ui/styles'
import { fade } from 'material-ui/utils/colorManipulator'

let createStoreWithThunk = applyMiddleware(thunkMiddleware)(createStore)
const persistedState = loadState()
let store = createStoreWithThunk(proj3, persistedState)

store.subscribe( () => {
	saveState(store.getState())
})

injectTapEventPlugin()

const muiTheme = getMuiTheme({
  fontFamily: 'FiraSans-Regular',
  palette: {
    primary1Color: _colors.red600,
    primary2Color: _colors.red600,
    primary3Color: _colors.grey400,
    accent1Color: _colors.pinkA200,
    accent2Color: _colors.grey100,
    accent3Color: _colors.grey500,
    textColor: _colors.darkBlack,
    secondaryTextColor: fade(_colors.darkBlack, 0.54),
    alternateTextColor: _colors.white,
    canvasColor: _colors.white,
    borderColor: _colors.grey300,
    disabledColor: fade(_colors.darkBlack, 0.3),
    pickerHeaderColor: _colors.cyan500,
    clockCircleColor: fade(_colors.darkBlack, 0.07),
    shadowColor: _colors.fullBlack,
  },
})

ReactDOM.render((
  <Provider store={ store }>
  	<MuiThemeProvider muiTheme={ muiTheme }>
    	<App />
    </MuiThemeProvider>
  </Provider>),
  document.getElementById('root')
)
