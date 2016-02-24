import React, { Component, PropTypes } from 'react';
import _ from 'underscore';

import h from 'utils/helpers';

import './Content.css';


class Content extends Component {

    componentWillMount() {
        this.setState({ content_types: [
            'results_notes',
            'system',
            'organ',
            'effect',
            'effect_subtype',
        ]});
    }


    render() {
        let { endpoint } = this.props,
            content = _.map(this.state.content_types, (type) => {
                return endpoint[type] ? <p key={type}><b><u>{h.caseToWords(type)}</u></b>: {endpoint[type]}</p> : null;
            });
        return (
            <div className='extraContent'>
                {content}
            </div>
        );
    }
}

Content.propTypes = {
    endpoint: PropTypes.shape({
        results_notes: PropTypes.string,
        system: PropTypes.string,
        organ: PropTypes.string,
        effect: PropTypes.string,
        effect_subtype: PropTypes.string,
    }).isRequired,
};

export default Content;
