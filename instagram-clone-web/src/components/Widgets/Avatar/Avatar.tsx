import React, { FC } from 'react'
import './Avatar.scss'

type Props = {
  src?: string
}

const Avatar: FC<Props> = ({ src }) => {
  return (
    <div className='avatar'>
      <img
        src={
          src ||
          'https://media.istockphoto.com/vectors/user-icon-flat-isolated-on-white-background-user-symbol-vector-vector-id1300845620?b=1&k=20&m=1300845620&s=170667a&w=0&h=JbOeyFgAc6-3jmptv6mzXpGcAd_8xqkQa_oUK2viFr8='
        }
      />
    </div>
  )
}

export default Avatar
