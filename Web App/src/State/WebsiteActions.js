export const LOADING_RECIPE = 'LOADING_RECIPE'

function loadingRecipe(){
	return {
		type: LOADING_RECIPE,
		isFetching: true,
	}
}

export function loadRecipe(){
	return dispatch => {
		dispatch(loadingRecipe)
	}
}