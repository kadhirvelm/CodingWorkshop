import { combineReducers } from 'redux'
import { routerReducer } from 'react-router-redux'

import {
	LOADING_RECIPE
} from './WebsiteActions'

function website(state = {}, action) {
	switch(action.type){
		case LOADING_RECIPE:
			return Object.assign({}, state)
		default:
			return state
	}
}

import { reducer } from 'redux-form'

const proj3 = combineReducers({
	website,
	routing: routerReducer,
	form: reducer
})

export default proj3