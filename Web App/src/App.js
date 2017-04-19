import React from 'react'
import { mapStateToProps } from './State/StateMethods'
import { connect } from 'react-redux'

import Flexbox from 'flexbox-react'

class App extends React.Component {

  constructor(props){
    super(props)
    this.state = this.propsConst(props)
  }

  propsConst = (props) => {
    return ({
      dispatch: props.dispatch,
    })
  }

  componentWillReceiveProps(nextProps){
    this.setState(this.propsConst(nextProps))
  }

  render() {
    return (
      <Flexbox flexDirection='column'>
        <div> 'Hello World' </div>
      </Flexbox>
    )
  }
}

export default connect(mapStateToProps)(App)
