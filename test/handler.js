const { expect } = require('chai');
const { hello } = require('../handler');

describe('hello function', () => {
  it('should return a hello message with input', async () => {
    const event = { someKey: 'someValue' };
    const result = await hello(event);

    expect(result.statusCode).to.equal(200);
    expect(result.body).to.be.a('string');

    const body = JSON.parse(result.body);
    expect(body).to.have.property('message', 'Hola, mundo!');
    expect(body).to.have.property('input').deep.equal(event);
  });
});
